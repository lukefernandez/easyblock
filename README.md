# easyblock

> An extremely light-weight website blocker.

## Overview

Why do I need a heavy-weight browser extension or clunky service running on my machine to block a few websites?
I think a website blocker should be something that:

1. Blocks the sites that I want to block (for me, domains and subdomains are sufficient)
2. Can be turned on and off with ease
3. Is light-weight
4. Is open-source (I want to know what is happening under the covers)

`easyblock` is designed with these criteria in mind.

## Usage

![easyblock](./easyblock.svg)

To use `easyblock`, simply put an `.easyblock` file in your home directory (`~`) with a domain on each line.

Here is an example configuration:

```
www.google.com
news.google.com
www.amazon.com
www.instagram.com
www.facebook.com
www.reddit.com
```

Then, to start blocking, run:

```bash
sudo python3 easyblock.py on
```

To stop blocking, run:

```bash
sudo python3 easyblock.py off
```

It's really that easy!

## Tested On

- macOS Catalina 10.15.4
- Ubuntu 20.04
