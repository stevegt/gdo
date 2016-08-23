# Governance of Distributed Organizations

Not a whole lot here yet -- throwing this together quickly for
discussion at the [Aug 2016 Nation of
Makers](https://www.whitehouse.gov/nation-of-makers) session.  As of
this writing still scraping together/refactoring code from
miscellaneous directories on my hard drive, most of which will land in
the [lab directory](lab) first.

## Overview

A distributed-ledger system suitable for hosting smart contracts and
running on IoT devices.  A few example applications:

- Organizational governance
- Workflow
- Training and certification
- Accounting
- Inventory control
- Door access control
- Machine lockout
- Membership
- Reservations
- Data storage and backups
- Operating system and disk image management
- IoT 

We accomplish all this using a (relatively) simple model:  Distributed
applications (dapps) running in Linux containers managed by a
distributed ledger, hosted in a distributed version control system
that performs content-defined chunking to store and ship around large
blobs, including the container images themselves.

The development roadmap, then, is (relatively) straightforward:
Implement things in reverse order of the above paragraph.  Beg,
borrow, and paste where possible, take advantage of existing code and
libraries such as libcontainer, ledger-cli, and libgit2, and become
self-hosting early.

Compared to e.g. Ethereum or HyperLedger, we'd like to target more of
a git-like version control model, allowing forking and interbranch
consensus, rather than a single linear blockchain.  For
turing-complete smart contracts, we simply use Linux containers --
this allows dapps to be written in any language executable on Linux.

We'll use test-driven consensus (proof of merge), where new blocks are
tested by one or more dapps, rather than use a hardcoded proof-of-work
algorithm.  Not requiring a compute-intensive proof of work means
single-board computers such as BeagleBone or Raspberry Pi can host
full nodes.

## Example

Maker space door access control, for instance, could be based on an
existing open source project such as
https://github.com/makeitlabs/doorbot, living in a container, with
modifications to have it communicate with membership, accounting, and
certification dapps, each in their own containers.  Comms are via the
blockchain, and all of this runs on localhost, as opposed to talking
to a central SQL db on a server somewhere else.  Each door can have
its own Raspberry Pi-sized host.  These will check and log access
events as usual even during network outages, and the blockchain's
distributed consensus protocol will resync records when the network
comes back up.

## References

Shares a few concepts with HyperLedger, Ethereum, Docker, Ledger-cli,
git, and git-annex.  Builds on earlier work and prototyping at
github.com/stevegt/librabinpoly and github.com/stevegt/git-devops.  

## Open Questions

- If forks are allowed (depending on dapp) and there can be multiple
  roots as well as multiple heads, then is this a "blockmesh" instead
  of a blockchain?
