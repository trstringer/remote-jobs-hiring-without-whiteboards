# Remote-friendly companies that potentially don't whiteboard during hiring

There are a couple of great lists out there for people looking for a great fit. Two common requirements for developers are remote-friendly jobs, and likewise developers looking to *not* have the whiteboarding interview experience.

Thankfully, members of the community have create these two lists...

- [remote-jobs](https://github.com/jessicard/remote-jobs) by [jessicard](https://github.com/jessicard)
- [hiring-without-whiteboards](https://github.com/poteto/hiring-without-whiteboards) by [poteto](https://github.com/poteto)

## ...sooooo what is this? :neutral_face:

This is just a little Python script that finds companies existing in both lists. Think of it like this...

![chart](./images/chart.png)

This script gets the intersection of remote jobs and companies that hire without whiteboards.

## Setup/Run

```
$ git clone https://github.com/tstringer/remote-jobs-hiring-without-whiteboards.git
$ cd remote-jobs-hiring-without-whiteboards
$ python3 app.py
```

## Current list :newspaper:

- Articulate
- Auth0
- Automattic
- Basecamp
- Chargify
- CircleCI
- DroneDeploy
- GitPrime
- HE:labs
- Heap
- Hireology
- InQuicker
- Intercom
- Librato
- Litmus
- Mapbox
- NodeSource
- Netguru
- Platform.sh
- Wildbit
- X-Team

## Future/To-Do

- Have a scheduled task that automatically runs the script and updates the list of companies

## Issues/Bugs

This was a super quick and ugly script with funny regular expressions. There's a great chance of a bug here. Open an issue, or better create a pull request!
