# autocosmo
make actually portable executables (APEs) that run on Linux, Mac, Windows, FreeBSD, OpenBSD, NetBSD, BIOS, and more on AMD64 and ARM64 architectures using cosmo.zip[1] with minimal effort

## example usage

- dependencies: `wget` maybe `python` with `pip`

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
- [x] download and pack dependencies (`pip download [package-name]`)[*]
- [x] fully document python dependency packing
- [ ] automate python dependency download and packaging
- [ ] extract dependencies from .py file & inject import redirect (do I need to modify the source code or can this be injected without modifying the code? is there a way to just change the global location or something like that?)
- [ ] try for a gui? run http server and spawn browser? is it possible to package multi-platform qt and detect the platform at runtime?
- [ ] will this work as an effective reverse-engineering prevention that would even the exposure between distributing c-dervied binary and python-derived binaries? fire up ghidra and find out!!
- [ ] what does this enable? combined with content addressable language features and a trust/verification mechanism to ensure the code you're running is the code you intend to be running this could enable some exciting distributed systems possibilities

# testing - working
- [x] test on my mac in a nix-shell with py dependencies installed
- [x] test on my mac in a nix-shell without py dependencies installed
- [ ] test on jetson
- [ ] test on raspberrypi
- [ ] test on linux
- [ ] test on x86 mac
- [ ] test on windows
- [ ] test on old mac
- [ ] test on old windows
- [ ] test on weird stuff as you come across it

# more inspiration / depth:

## quotes & footnotes

> [1] "Cosmopolitan Libc makes C a build-once run-anywhere language, like Java, except it doesn't need an interpreter or virtual machine. Instead, it reconfigures stock GCC and Clang to output a POSIX-approved polyglot format that runs natively on Linux + Mac + Windows + FreeBSD + OpenBSD + NetBSD + BIOS with the best possible performance and the tiniest footprint imaginable."

> [2] "One day, while studying old code, I found out that it's possible to encode Windows Portable Executable files as a UNIX Sixth Edition shell script, due to the fact that the Thompson Shell didn't use a shebang line. Once I realized it's possible to create a synthesis of the binary formats being used by Unix, Windows, and MacOS, I couldn't resist the temptation of making it a reality, since it means that high-performance native code can be almost as pain-free as web apps. [Here's how it works:](https://justine.lol/ape.html)"

> [3] "I started a project called [Cosmopolitan](https://github.com/jart/cosmopolitan) which implements the [αcτµαlly pδrταblε εxεcµταblε](https://raw.githubusercontent.com/jart/cosmopolitan/1.0/ape/ape.S) format. I chose the name because I like the idea of having the freedom to write software without restrictions that transcends traditional boundaries. My goal has been helping C become a build-once run-anywhere language, suitable for greenfield development, while avoiding any assumptions that would prevent software from being shared between tech communities."

> [4] "Please note this is intended for people who don't care about desktop GUIs, and just want stdio and sockets without devops toil"

> Long Lifetime Without Maintenance
One of the reasons why I love working with a lot of these old technologies, is that I want any software work I'm involved in to stand the test of time with minimal toil. Similar to how the Super Mario Bros ROM has managed to survive all these years without needing a GitHub issue tracker.

> I believe the best chance we have of doing that, is by gluing together the binary interfaces that've already achieved a decades-long consensus, and ignoring the APIs. For example, here are the magic numbers used by Mac, Linux, BSD, and Windows distros. They're worth seeing at least once in your life, since these numbers underpin the internals of nearly all the computers, servers, and phones you've used.

> If we focus on the subset of numbers all systems share in common, and compare it to their common ancestor, Bell System Five, we can see that few things about systems engineering have changed in the last 40 years at the binary level. Magnums are boring. Platforms can't break them without breaking themselves. Few people have proposed visions over the years on why UNIX numerology needs to change.

> ^^ (https://justine.lol/ape.html)

> [5] the dream: ["Not just python scripts, you can package any C code as well. We've used it to compile up a "python.com" APE file with a python 3.11 interpreter that has lots of packages (including C extensions) that we can just drop straight into old airgapped lab instrument computers and get a modern python data analysis suite up and running."](https://news.ycombinator.com/item?id=39114248)

> more: "Now we can combine this with the xlcalculator package and transpile models built in Excel right down to C code and build it as a portable executable."

# [*] packing python dependencies
1. I have a py script that needs beautiful soup. ran it through my cosmo builder and it is complaining about missing soup
2. I tell pip to download soup to ./Lib
3. I manually unzip the python wheels in place
4. then insert a line before my soup import so it imports from a file path and not the pip cache
5. pack all of that up into the zip/fat binary with the import path structure intact
6. then it runs. wtf!?

detail:

```
pip3 download requests -d Lib
pip3 download beautifulsoup4 -d Lib

cd Lib
unzip requests-2.31.0-py3-none-any.whl
unzip certifi-2023.11.17-py3-none-any.whl
unzip ... (unzip every .whl file)

cd ..
./autocosmo.sh network_details.py

./network_detail.com
```
