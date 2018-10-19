# Toy

Some practical tools. Just have fun.

## Scripts

```bash
.
├── LICENSE
├── README.md
├── clone_all_projects.sh
├── mongodb_checker.sh
├── others
│   ├── etc-logrotate.d-mongod
│   └── etc-systemd-system-mongodb.service
├── prank.sh
└── syn_gitlab_github.py
```

* prank.sh: Send a message to play a prank on somebody
* mongodb_checker.sh: Check the status of mongoDB
* clone_all_projects.sh: Clone all gitlab's projects to current directory
* syn_gitlab_github.py: Sync all gitlab projects to github (Must be placed on the root directory of all gitlab projects)
* Directory others:
  * etc-logrotate.d-mongod: Manage the automatic rotation and compression of mongoDB log file (/etc-logrotate.d/mongod & /var/log/)
  * etc-systemd-system-mongodb: Run mongoDB as a service using systemd (/etc/systemd/system/mongodb)

## Usages

* prank.sh: `sudo bash -x bingo.sh [name] [msg]`
* mongodb_checker.sh: `sudo bash -x mongodb_checker.sh` (P.S. Highly recommended to use it with crontab)
* clone_all_projects.sh: `bash -x clone_all_projects.sh [gitlab url] [gitlab token]`
* syn_gitlab_github.py: `python3 syn_gitlab_github.py -gh [github account] -gl [gitlab account] -url [gitlab url]`

## License

This software is licensed under the [MIT license](http://en.wikipedia.org/wiki/MIT_License).

```bash
MIT License

Copyright (c) 2018 Carson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

© 2018 Carson Wang.
