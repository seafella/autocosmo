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
- [ ] seems like the ./ before the .py filename is required for the ref to work. add it if it's missing?
- [ ] automate python dependency download and packaging
- [ ] extract dependencies from .py file & inject import redirect (do I need to modify the source code or can this be injected without modifying the code? is there a way to just change the global location or something like that?)
- [ ] try for a gui? [run http server](https://github.com/jart/cosmopolitan/issues/35#issuecomment-773209579) ([redbean](https://redbean.dev/)) and spawn browser? is it possible to package multi-platform qt and detect the platform at runtime? ([cosmo git discussion](https://github.com/jart/cosmopolitan/issues/35)), [OpenGL implementation](https://github.com/jacereda/cosmogfx)
- [ ] will this work as an effective reverse-engineering prevention that would even the exposure between distributing c-dervied binary and python-derived binaries? fire up ghidra and find out!!
- [ ] what does this enable? combined with content addressable language features and a trust/verification mechanism to ensure the code you're running is the code you intend to be running this could enable some exciting distributed systems possibilities
- [ ] run on bare metal / bios / uefi

  [some discussion](https://github.com/jart/cosmopolitan/issues/12#issuecomment-783101313)
- [ ] However portability isn't the only selling point. Cosmo Libc will make your software faster and use less memory too.

  [Search for `MODE=tinylinux` in the https://github.com/jart/cosmopolitan#getting-started section of the README. If you use that build mode, then hello world for x86 linux is only 8kb in size. It's very similar to what you'd expect from Musl Libc. All the Windows / BSD / Mac / BIOS stuff gets removed from the compilation.](https://news.ycombinator.com/item?id=38106371)

  [That predefined mode is actually a friendly wrapper around a more generalized platform support system Cosmopolitan offers, which is called `-DSUPPORT_VECTOR` where you can define a bitset of specifically what platforms you want to be supported. Then dead code elimination takes care of the rest. The same concept also generally applies to microarchitecture support, where you can have as much or as little runtime dispatching as you want.](https://news.ycombinator.com/item?id=38106371)
- [ ] what about GPUs?
    1. [no gpu but working toward it](https://github.com/trholding/llama2.c)
    1. [just a wrapper](https://llm.datasette.io/)
    1. [more discussion](https://news.ycombinator.com/item?id=38102843)
- [ ] ["Installing CPython extensions like this is an unsolved problem, but I think there might be some interesting workarounds possible."](https://news.ycombinator.com/item?id=38103827)
- [ ] something something nix ...





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

> [6] > POSIX even changed their rules about binary in shell scripts specifically to let us do it.

> See https://austingroupbugs.net/view.php?id=1250 and https://austingroupbugs.net/view.php?id=1226

---

> Kinda feels like they are super intelligent alien beings from another planet trying to save us from software bloat and fragmentation.

> POSIX even changed their rules about binary in shell scripts specifically to let us do it.

> [I don't know what to say.](https://news.ycombinator.com/item?id=38103124)

> [7] speed! (& (what about (emacs)))

> [The end result is that if you switch your Linux build process to use cosmocc instead of cc then the programs you build, e.g. Bash and Emacs, will just work on the command prompts of totally different platforms like Windows and MacOS, and when you run your programs there, it'll feel like you're on Linux. However portability isn't the only selling point. Cosmo Libc will make your software faster and use less memory too. For example, when I build Emacs using the cosmocc toolchain, Emacs thinks it's building for Linux. Then, when I run it on Windows:](https://news.ycombinator.com/item?id=38101995)

> [It actually goes **2x** faster than the native WIN32 port that the Emacs authors wrote on their own. Cosmo Emacs loads my dotfiles in 1.2 seconds whereas GNU Emacs on Windows loads them in 2.3 seconds.](https://news.ycombinator.com/item?id=38101995)

- [8] portable agents!

> all so that the same binary runs on multiple operating systems, which isn’t actually very useful.

> I like to mention my use case when this comes up: my log file viewer (https://lnav.org) uploads an agent to remote hosts in order to tail log files on that [host](https://lnav.org/2021/05/03/tailing-remote-files.html). While lnav itself is not built using cosmo, the agent is. So, it works on multiple OSs without having to compile and include multiple versions of the agent.
(https://news.ycombinator.com/item?id=38109519)

- [9] interesting uses
    1. printvideo renders .mpg videos in the terminal
    1. nesemu1 play nintendo games in the terminal
    1. apelife conway's game of life tui + gui
    1. memzoom process/file memory monitor
    1. blinkenlights pc emulating visualizer debugger
    1. printimage prints png/jpg files in the terminal
    1. kilo antirez's famous text editor
    - https://github.com/jart/cosmopolitan/issues/35#issuecomment-770109680


# [*] packing python dependencies
1. I have a py script that needs beautiful soup. ran it through my cosmo builder and it is complaining about missing soup
2. I tell pip to download soup to ./Lib
3. I manually unzip the python wheels in place
4. then insert a line before my soup import so it imports from a file path and not the pip cache
5. pack all of that up into the zip/fat binary with the import path structure intact
6. then it runs. wtf!?

detail:

```
if no wget on local download and use: https://cosmo.zip/pub/cosmos/bin/wget

# auto:

wget https://raw.githubusercontent.com/seafella/autocosmo/main/build_example_network_details.sh;chmod +x build_example_network_details.sh;./build_example_network_details.sh

# manual:

wget https://cosmo.zip/pub/cosmos/bin/python
wget https://cosmo.zip/pub/cosmos/bin/unzip
wget https://raw.githubusercontent.com/seafella/autocosmo/main/autocosmo.sh
wget https://raw.githubusercontent.com/seafella/autocosmo/main/network_details.py

chmod +x ./python
chmod +x ./unzip
chmod +x ./autocosmo.sh

mkdir Lib
./python -m pip download requests beautifulsoup4 -d Lib
for whl in Lib/*.whl; do unzip "$whl" -d Lib/; done

./autocosmo.sh ./network_details.py
./network_details
```

^ [suggestions to improve this](https://news.ycombinator.com/item?id=38103827)
