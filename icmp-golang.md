# Building ICMPv6 Messages using `google/gopacket`

For a few months in 2018 I was working at a company working on network programming with GoLang. We sometimes need to write test code which sends individual packets using protocols, such as ARP or ICMPv6. At one point I needed to send ICMPv6 Neighbor Solicitation messages using [`google/gopacket`](https://godoc.org/github.com/google/gopacket) - and found there wasn’t much material online about how to get it to work. So I thought I’d best write one, and then let it sit around for 6 months before actually publishing it online.

Overall, I’m going to take it pretty slow, but if you want to you can skip to the very end where the entire program is put together.

---

For example, let's say an ICMPv6 Neighbor Solicitation message is needed, as described in [RFC 4861 Section 4.3](https://tools.ietf.org/html/rfc4861#section-4.3) - something like this hex dump:

```
33 33 ff 00 00 01 0e 31 b1 c5 4c f6 86 dd 60 00
00 00 00 20 3a ff fd 10 00 00 00 00 00 00 00 00
00 00 00 00 00 02 ff 02 00 00 00 00 00 00 00 00
00 01 ff 00 00 01 87 00 72 8c 00 00 00 00 fd 10
00 00 00 00 00 00 00 00 00 00 00 00 00 01 01 01
0e 31 b1 c5 4c f6
```

That hex dump represents an ICMPv6 Neighbor Solicitation message. If the above were [imported as a hex dump into Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html), the packet summary would read something like this:

| Source  | Destination    | Protocol | Length | Info                                                     |
| ------- | -------------- | -------- | ------ | -------------------------------------------------------- |
| fd10::2 | ff02::1:ff00:1 | ICMPv6   | 86     | Neighbor Solicitation for fd10::1 from 0e:31:b1:c5:4c:f6 |

... and Wireshark would make it easy to see the encapsulated layers this packet is organized into:

* First, the Ethernet II layer:  
  ```
  33 33 ff 00 00 01 0e 31 b1 c5 4c f6 86 dd`
  ```

* Next, an Internet Protocol Version 6 layer:  
  ```
  -- -- -- -- -- -- -- -- -- -- -- -- -- -- 60 00
  00 00 00 20 3a ff fd 10 00 00 00 00 00 00 00 00
  00 00 00 00 00 02 ff 02 00 00 00 00 00 00 00 00
  00 01 ff 00 00 01
  ```

* And lastly an Internet Control Message Protocol v6 layer:  

  ```
  -- -- -- -- -- -- 87 00 72 8c 00 00 00 00 fd 10
  00 00 00 00 00 00 00 00 00 00 00 00 00 01 01 01
  0e 31 b1 c5 4c f6
  ```

To build this packet in golang - or at least one like it - each of these layers needs to be constructed individually, using [`google/gopacket/layers`](https://godoc.org/github.com/google/gopacket/layers).

## The Ethernet Layer

The packet's Ethernet layer is actually composed of three parts:
* a destination address - MAC address `33-33-ff-00-00-01`
* a source address - MAC address `0e-31-b1-c5-4c-f6`
* an EtherType - `0x86dd`, specifying that the next layer is IPv6 per [RFC 7042](https://tools.ietf.org/html/rfc7042#appendix-B.1)

Conveniently, the `google/gopacket/layers` package has a `layers.Ethernet` type with exactly those fields:

```
	ethLayer := layers.Ethernet{
		SrcMAC:       srcMacAddr,
		DstMAC:       dstMacAddr,
		EthernetType: layers.EthernetTypeIPv6,
	}
```

But what values should be used for the `SrcMAC` and `DstMAC`? The source address is easy - it should be the MAC address for the network interface from which the message will be sent. That can be determined pretty easily using [`vishvananda/netlink`](https://godoc.org/github.com/vishvananda/netlink#Handle.LinkByName):

```
	intfName := "eth0" // TODO: change name of networking interface to one which exists on one's personal computer

	intf, err := netlink.LinkByName(intfName)
	if err != nil {
		// handle the error
	}

	srcMacAddr := intf.Attrs().HardwareAddr
```

The destination address is a little trickier, since Neighbor Solicitation messages are supposed to be sent to an [IPv6 solicited-node multicast address](https://tools.ietf.org/html/rfc4861#section-2.3). That means the destination MAC will have to use an Ethernet multicast address as described in [RFC 2464](https://tools.ietf.org/html/rfc2464#section-7):

> An IPv6 packet with a multicast destination address DST, consisting
> of the sixteen octets DST[1] through DST[16], is transmitted to the
> Ethernet multicast address whose first two octets are the value 3333
> hexadecimal and whose last four octets are the last four octets of
> DST.

So the destination MAC address will be determined by the bytes in the destination IPv6 address, which in turn should be a solicited-node multicast address as described in [RFC 429, Section 2.7.1](https://tools.ietf.org/html/rfc4291#section-2.7.1):

> Solicited-Node multicast address are computed as a function of a
> node's unicast and anycast addresses.  A Solicited-Node multicast
> address is formed by taking the low-order 24 bits of an address
> (unicast or anycast) and appending those bits to the prefix
> FF02:0:0:0:0:1:FF00::/104 resulting in a multicast address in the
> range

The `google/gopacket` library doesn't currently offer any convenience methods for creating these multicast addresses - [nor does package `net`](https://github.com/golang/go/issues/25257) - but it won't take much to do it the old fashioned way:

```
	ipv6Addr := net.ParseIP("fd10::1") // fd10::1 was the target IP for our solicitation
	solicitedMulticastIPAddr, _, _ := net.ParseCIDR("FF02:0:0:0:0:1:FF00::/104")
	for i:=len(ipv6Addr)-3; i<len(ipv6Addr); i++ {
		solicitedMulticastIPAddr[i] = ipv6Addr[i]
	}

	byteArr := []byte {0x33, 0x33}
	// the last 32 bits (last 4 bytes) come from the IPv6 multicast address
	for i:=len(ipV6Addr)-4; i<len(solicitedMulticastIPAddr); i++{
		byteArr = append(byteArr, solicitedMulticastIPAddr[i])
	}

	dstMacAddr := net.HardwareAddr(byteArr)
```

## The IPv6 Layer

Like the Ethernet layer which came before, the packet's IPv6 layer is actually composed of several parts:
* the 4-bit IP version - always `6` according to [RFC 1883 section 3](https://tools.ietf.org/html/rfc1883#section-3)
* the 4-bit Priority and 24-bit Flow Label - all zeroes in our example and not really relevant to this exercise
* a Payload Length - `0x0020` or 32
* the Next Header - `0x3a` or ICMPv6 as per [RFC 4443 secion 2.3](https://tools.ietf.org/html/rfc4443#section-2.3)
* a Hop Limit - `0xff` or 255, but not really relevant to this exercise
* the IPv6 Source Address - 16-byte address of the originator of the packet, in this case `fd10:0000:0000:0000:0000:0000:0000:0002` or just `fd10::2`
* the IPv6 Destination Address - 16-byte address of the intended recipient of the packet, in this case the solicited multicast address `ff02:00:00:00:00:00:00:00:00:00:01:ff:00:00:01`

Like with the Ethernet layer, the `google/gopacket/layers` package has a convenient `layers.IPv6` type with those fields:

```
	ipV6Layer := layers.IPv6{
		SrcIP: srcIPAddr,
		DstIP: solicitedMulticastIPAddr,
		Version: 6,
		NextHeader: layers.IPProtocolICMPv6,
		HopLimit: 255,
	}
```

The source address can be determined programmatically by inspecting that network interface using using the golang [`net` package](https://golang.org/pkg/net/):

```
	intfName := "eth0" // TODO: change name of networking interface to one which exists on one's personal computer

        intf, err := net.InterfaceByName(intfName)
        if err != nil {
                fmt.Printf("failed to get intf - %v", err)
                return err
        }

        addrs, err := intf.Addrs()
        if err != nil {
                fmt.Printf("failed to get intf addresses - %v", err)
                return err
        }
        for _, addr := range addrs {
                var ip net.IP
                switch addr := addr.(type) {
                case *net.IPAddr:
                        ip = addr.IP
                case *net.IPNet:
                        ip = addr.IP
                }
		// Maybe check that it's not a link local IP address?
                fmt.Println("%s", ip)
        }
```

... and the destination address - a solicited-node multicast address - was already constructed while populating values for the Ethernet layer.

Of note is that the length field has been ommited from the created `layers.IPv6` instance. While there is a [`Length` field on the `layers.IPv6` struct](https://github.com/google/gopacket/blob/28a83096fbe78359d86ddf0387ea7395f66321e6/layers/ip6.go#L34), it's best not to specify its value and to calculate instead, [while serializing all the layers into a packet](https://godoc.org/github.com/google/gopacket#SerializeOptions).


## The ICMPv6 Layer

The last 32 bytes of the packet are the ICMPv6 Layer and its various fields:
* the ICMPv6 Type and Code - `0x87` (135) and `0x00` (0) for Neighbor Solicitation, as per [RFC 4861 section 4.3](https://tools.ietf.org/html/rfc4861#section-4.3)
* the ICMP Checksum - for this packet it's `0x728c`
* 4 reserved bytes, `0x00000000`
* the IPv6 Target Address - the 16-byte IP Address of the neighbor we're attempting to solicit a response from
* An 8-byte Source Link-Layer Address option, as described in [RFC 4861 section 4.6.1](https://tools.ietf.org/html/rfc4861#section-4.6.1), with:
  * Option Type `0x01`
  * Length `0x01`
  * Link Layer Address `0e-31-b1-c5-4c-f6` - which matches the source address from the Ethernet layer

Like the layers which came before, the `google/gopacket/layers` package does have a `layers.ICMPv6` type which can be used to create the ICMPv6 layer. However, the `layers.ICMPv6` struct must be used in conjection with another layer like `layers.ICMPv6NeighborSolicitation`:

```
	targetIPAddr := net.ParseIP("fd10::1")

	icmpv6Layer := layers.ICMPv6{
		TypeCode: layers.CreateICMPv6TypeCode(layers.ICMPv6TypeNeighborSolicitation, 0),
	}

	ndLayer := layers.ICMPv6NeighborSolicitation{
		TargetAddress: targetIPAddr,
		Options: layers.ICMPv6Options{
			layers.ICMPv6Option{
				Type: layers.ICMPv6OptSourceAddress,
				Data: srcMacAddr,
			},
		},
	}

	err = icmpv6Layer.SetNetworkLayerForChecksum(&ipV6Layer)
	if err != nil {
		return fmt.Errorf("Error while setting the checksum network layer for ICMPv6 layer: %s", err)
	}
```

Like the IPv6 layer, it has a `Length` which is best left blank [until serializing all the layers into a packet](https://godoc.org/github.com/google/gopacket#SerializeOptions). The same goes for the `Checksum` field, although the network layer to use while calculating the checksum - the IPv6 layer - must be specified using `SetNetworkLayerForChecksum(...)`.

## Serializing the Layers

Once all the fields for each layer of the message are populated (except lengths and checksums) the layers can be serialized into a byte array using the [`SerializeLayers(...)`](https://godoc.org/github.com/google/gopacket#SerializeLayers) function in `google/gopacket`. The second argument - of type `SerializeOptions` - can specify that any `Lengths` or `Checksum` values on any layers should be calculated and be populated:

```
	buffer := gopacket.NewSerializeBuffer()
	options := gopacket.SerializeOptions{
		FixLengths:       true,
		ComputeChecksums: true,
	}
	err = gopacket.SerializeLayers(buffer, options, &ethLayer, &ipV6Layer, &icmpv6Layer, &ndLayer)
	if err != nil {
		return fmt.Errorf("unable to serialize layers for Neighbor Solicitation request: %s", err)
	}
```

## Putting It All Together

Here's the final script. Its output can be piped into a file and [imported as a hex dump into Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html) to confirm the resulting packet is valid:

```
package main

import (
	"fmt"
	"encoding/hex"
	"net"
	"github.com/vishvananda/netlink"
	"github.com/google/gopacket"
	"github.com/google/gopacket/layers"
)

func main() {
	intfName := "sw1p2"

	link, err := netlink.LinkByName(intfName)
	if err != nil {
		fmt.Printf("Error from netlink.LinkByName(...): %s\n", err)
		return
	}

	srcMacAddr := link.Attrs().HardwareAddr

	ipv6Addr := net.ParseIP("fd10::1") // fd10::1 was the target IP for our solicitation
	solicitedMulticastIPAddr, _, _ := net.ParseCIDR("FF02:0:0:0:0:1:FF00::/104")
	for i:=len(ipv6Addr)-3; i<len(ipv6Addr); i++ {
		solicitedMulticastIPAddr[i] = ipv6Addr[i]
	}

	byteArr := []byte {0x33, 0x33}
	// the last 32 bits (last 4 bytes) come from the IPv6 multicast address
	for i:=len(ipv6Addr)-4; i<len(solicitedMulticastIPAddr); i++{
		byteArr = append(byteArr, solicitedMulticastIPAddr[i])
	}

	dstMacAddr := net.HardwareAddr(byteArr)

	ethLayer := layers.Ethernet{
		SrcMAC:       srcMacAddr,
		DstMAC:       dstMacAddr,
		EthernetType: layers.EthernetTypeIPv6,
	}

        intf, err := net.InterfaceByName(intfName)
        if err != nil {
                fmt.Printf("failed to get intf - %v", err)
                return
        }

	var srcIPAddr net.IP
        addrs, err := intf.Addrs()
        if err != nil {
                fmt.Printf("failed to get intf addresses - %v", err)
                return
        }
        for _, addr := range addrs {
                var ip net.IP
                switch addr := addr.(type) {
                case *net.IPAddr:
                        ip = addr.IP
                case *net.IPNet:
                        ip = addr.IP
                }
		isIPv6 := !ip.To4().Equal(ip)
		if isIPv6 && !ip.IsLinkLocalUnicast() { // this is an IPv6 address
			srcIPAddr = ip
			break
		}
        }

	ipV6Layer := layers.IPv6{
		SrcIP: srcIPAddr,
		DstIP: solicitedMulticastIPAddr,
		Version: 6,
		NextHeader: layers.IPProtocolICMPv6,
		HopLimit: 255,
	}

	targetIPAddr := net.ParseIP("fd10::1")

	icmpv6Layer := layers.ICMPv6{
		TypeCode: layers.CreateICMPv6TypeCode(layers.ICMPv6TypeNeighborSolicitation, 0),
	}

	ndLayer := layers.ICMPv6NeighborSolicitation{
		TargetAddress: targetIPAddr,
		Options: layers.ICMPv6Options{
			layers.ICMPv6Option{
				Type: layers.ICMPv6OptSourceAddress,
				Data: srcMacAddr,
			},
		},
	}

	err = icmpv6Layer.SetNetworkLayerForChecksum(&ipV6Layer)
	if err != nil {
		fmt.Printf("Error while setting the checksum network layer for ICMPv6 layer: %s", err)
		return
	}

	buffer := gopacket.NewSerializeBuffer()
	options := gopacket.SerializeOptions{
		FixLengths:       true,
		ComputeChecksums: true,
	}
	err = gopacket.SerializeLayers(buffer, options, &ethLayer, &ipV6Layer, &icmpv6Layer, &ndLayer)
	if err != nil {
		fmt.Printf("unable to serialize layers for Neighbor Solicitation request: %s", err)
		return
	}

	for i, b := range(buffer.Bytes()) {
		fmt.Printf("%s", hex.EncodeToString([]byte {b}))
		if i%16 == 15 {
			fmt.Println()
		} else {
			fmt.Print(" ")
		}
	}

	fmt.Println()

	return
}
```

