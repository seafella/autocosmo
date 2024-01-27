# autocosmo
make actually portable executables (APEs) that run on Linux, Mac, Windows, FreeBSD, OpenBSD, NetBSD, BIOS, and more on AMD64 and ARM64 architectures using cosmo.zip[1] with minimal effort

## example usage

- sample script included that logs ip address changes in org format
`./autocosmo.sh ./ip_changes_v2.0.1.py`

- replace the filename with your script
`./autocosmo.sh ./<your_file>.py`

## what is this!?

basically cosmo lets you run c code anywhere and you can build python to c. this project automates as much of the detail as possible

# shout out

- to [scrapscript](https://scrapscript.com/) for the inspo and [cosmo.zip](https://cosmo.zip/) for the binaries

- [cosmopolitan project](https://github.com/jart/cosmopolitan?tab=readme-ov-file)

- [also check out unison](https://www.unison-lang.org/)


# next up
- [ ] download and pack dependencies (`pip download [package-name]`)
- [ ] try for a gui? run http server and spawn browser? is it possible to package multi-platform qt and detect the platform at runtime?

more inspiration / depth:

the dream: ["Not just python scripts, you can package any C code as well. We've used it to compile up a "python.com" APE file with a python 3.11 interpreter that has lots of packages (including C extensions) that we can just drop straight into old airgapped lab instrument computers and get a modern python data analysis suite up and running."](https://news.ycombinator.com/item?id=39114248)

the nightmare: "Now we can combine this with the xlcalculator package and transpile models built in Excel right down to C code and build it as a portable executable."

# quotes & footnotes

> [1] "Cosmopolitan Libc makes C a build-once run-anywhere language, like Java, except it doesn't need an interpreter or virtual machine. Instead, it reconfigures stock GCC and Clang to output a POSIX-approved polyglot format that runs natively on Linux + Mac + Windows + FreeBSD + OpenBSD + NetBSD + BIOS with the best possible performance and the tiniest footprint imaginable."

> [2] "One day, while studying old code, I found out that it's possible to encode Windows Portable Executable files as a UNIX Sixth Edition shell script, due to the fact that the Thompson Shell didn't use a shebang line. Once I realized it's possible to create a synthesis of the binary formats being used by Unix, Windows, and MacOS, I couldn't resist the temptation of making it a reality, since it means that high-performance native code can be almost as pain-free as web apps. [Here's how it works:](https://justine.lol/ape.html)"

> [3] "I started a project called [Cosmopolitan](https://github.com/jart/cosmopolitan) which implements the [αcτµαlly pδrταblε εxεcµταblε](https://raw.githubusercontent.com/jart/cosmopolitan/1.0/ape/ape.S) format. I chose the name because I like the idea of having the freedom to write software without restrictions that transcends traditional boundaries. My goal has been helping C become a build-once run-anywhere language, suitable for greenfield development, while avoiding any assumptions that would prevent software from being shared between tech communities."

> [4] "Please note this is intended for people who don't care about desktop GUIs, and just want stdio and sockets without devops toil"

> Long Lifetime Without Maintenance
One of the reasons why I love working with a lot of these old technologies, is that I want any software work I'm involved in to stand the test of time with minimal toil. Similar to how the Super Mario Bros ROM has managed to survive all these years without needing a GitHub issue tracker.

> I believe the best chance we have of doing that, is by gluing together the binary interfaces that've already achieved a decades-long consensus, and ignoring the APIs. For example, here are the magic numbers used by Mac, Linux, BSD, and Windows distros. They're worth seeing at least once in your life, since these numbers underpin the internals of nearly all the computers, servers, and phones you've used.

> If we focus on the subset of numbers all systems share in common, and compare it to their common ancestor, Bell System Five, we can see that few things about systems engineering have changed in the last 40 years at the binary level. Magnums are boring. Platforms can't break them without breaking themselves. Few people have proposed visions over the years on why UNIX numerology needs to change.

> ^^ (https://justine.lol/ape.html)