# autocosmo
make actually portable executables (APEs) that run on Linux, Mac, Windows, FreeBSD, OpenBSD, NetBSD, BIOS, and more on AMD64 and ARM64 architectures using cosmo.zip[1] with minimal effort


## example usage

### sample script included that logs ip address changes in org format
`./autocosmo.sh ./ip_changes_v2.0.1.py`

## what is this!?

basically cosmo lets you run c code anywhere and you can build python to c. this project automates as much of the detail as possible

## 😁

shout out to [scrapscript](https://scrapscript.com/) for the inspo and [cosmo.zip](https://cosmo.zip/) for the binaries

[cosmopolitan project](https://github.com/jart/cosmopolitan?tab=readme-ov-file)



[1] "Cosmopolitan Libc makes C a build-once run-anywhere language, like Java, except it doesn't need an interpreter or virtual machine. Instead, it reconfigures stock GCC and Clang to output a POSIX-approved polyglot format that runs natively on Linux + Mac + Windows + FreeBSD + OpenBSD + NetBSD + BIOS with the best possible performance and the tiniest footprint imaginable."

[2] "One day, while studying old code, I found out that it's possible to encode Windows Portable Executable files as a UNIX Sixth Edition shell script, due to the fact that the Thompson Shell didn't use a shebang line. Once I realized it's possible to create a synthesis of the binary formats being used by Unix, Windows, and MacOS, I couldn't resist the temptation of making it a reality, since it means that high-performance native code can be almost as pain-free as web apps. [Here's how it works:](https://justine.lol/ape.html)"

[3] "I started a project called [Cosmopolitan](https://github.com/jart/cosmopolitan) which implements the [αcτµαlly pδrταblε εxεcµταblε](https://raw.githubusercontent.com/jart/cosmopolitan/1.0/ape/ape.S) format. I chose the name because I like the idea of having the freedom to write software without restrictions that transcends traditional boundaries. My goal has been helping C become a build-once run-anywhere language, suitable for greenfield development, while avoiding any assumptions that would prevent software from being shared between tech communities."