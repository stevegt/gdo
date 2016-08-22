# gdo
Governance of Distributed Organizations

Not a whole lot here yet -- throwing this together quickly for the [Aug 2016
Nation of Makers](https://www.whitehouse.gov/nation-of-makers) session.  

A distributed-ledger system suitable for hosting smart contracts.  A few
example applications:

- Organizational governance
- Accounting
- Workflow
- Training and certification
- Inventory control
- Door access control
- Machine lockout
- Membership
- Reservations
- Data storage and backups
- Host operating system and disk image management
- IoT 

We accomplish all this using a (relatively) simple model:  Distributed
applications running in Linux containers managed by a distributed ledger,
hosted in a distributed version control system which performs content-defined
chunking to store, trade, and ship around large blobs.  

The development roadmap, then, is (relatively) straightforward: Implement
things in reverse order of the above paragraph.  Beg, borrow, and paste where
possible, take advantage of existing code and libraries such as libgit2, and
become self-hosting early.

Compared to e.g. Ethereum or HyperLedger, we'd like to target more of a
git-like version control model, allowing forking and interbranch consensus,
rather than a single linear blockchain.  For turing-complete smart contracts,
we simply use Linux containers -- this should allows dapps to be written in any
language available on Linux.

Bullds on earlier work and prototyping at github.com/stevegt/librabinpoly and
github.com/stevegt/git-devops.  Shares a few concepts with HyperLedger,
Ethereum, Docker, Ledger-cli, ISconf, git, and git-annex.

Question for the intertubes:  If forks are allowed and there can be multiple
roots as well as multiple heads, then is this a "blockmesh" instead of a
blockchain?

