# Ryan Dellolio

Transformation leader and technologist at EY. Nights and weekends: running a home lab, writing software, sharing what might be helpful, sending fixes upstream.

[<img src="https://ryan.dellol.io/favicon-32.png" height="16" align="absmiddle" alt=""> ryan.dellol.io](https://ryan.dellol.io) | [<img src="https://api.iconify.design/fa6-brands/linkedin.svg?color=%230A66C2&height=16" height="16" align="absmiddle" alt=""> LinkedIn](https://www.linkedin.com/in/ryandellolio) | [<picture><source media="(prefers-color-scheme: dark)" srcset="https://api.iconify.design/fa6-brands/medium.svg?color=%23ffffff&height=16"><img src="https://api.iconify.design/fa6-brands/medium.svg?color=%23000000&height=16" height="16" align="absmiddle" alt=""></picture> Medium](https://medium.com/@ryandellolio) | [<picture><source media="(prefers-color-scheme: dark)" srcset="https://api.iconify.design/fa6-brands/x-twitter.svg?color=%23ffffff&height=16"><img src="https://api.iconify.design/fa6-brands/x-twitter.svg?color=%23000000&height=16" height="16" align="absmiddle" alt=""></picture> X](https://x.com/ryandellolio)

## Open source (upstream contributions)

**[openebs/mayastor-extensions #118](https://github.com/openebs/mayastor-extensions/pull/118)**, merged March 2023.
I was running a Talos Kubernetes cluster across my home lab and a cloud VM with OpenEBS Mayastor for
storage. A fresh install came up with every pod healthy and nothing working. I traced it to two services
the Helm chart defined as headless, which my network could not route to, so the core agent was never
reachable. Talked it through with a maintainer on the Kubernetes Slack and sent the fix. It shipped in
Mayastor v2.1.0 and is still in the chart.

**[thinq-connect/pythinqconnect #61](https://github.com/thinq-connect/pythinqconnect/pull/61)**, open.
While building lgac I worked out how the LG ThinQ app gets live updates: a mutual-TLS MQTT session to
AWS IoT Core. LG's own Python SDK asks that broker for a 6-second keep-alive. AWS silently rounds
anything under 30 up to 30, and MQTT 3.1.1 can't tell the client, so the SDK pinged five times too
often and dropped connections the broker thought were fine. One-number fix, found by reading the AWS
quotas page against my own client's behavior.

## Projects

| Project | What it is |
|---|---|
| [lgac](https://github.com/ryandellolio/lgac) | CLI and live TUI for LG ThinQ air conditioners over LG's official API, with a mutual-TLS MQTT push client. Node.js, no SDK. |
| [alpine-k8s-omni](https://github.com/ryandellolio/alpine-k8s-omni) | The `alpine/k8s` toolbox image with `talosctl` and `omnictl` added. [Docker Hub](https://hub.docker.com/r/ryandellolio/alpine-k8s-omni). |
| [ether](https://github.com/ryandellolio/ether) | Proof of concept for a DNS-based web content management system. |
| [fresh-kube](https://github.com/ryandellolio/fresh-kube) | Script that installs Kubernetes and Flannel without a package manager. |
