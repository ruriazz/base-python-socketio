## Short Deployment Guide

#### Proxy Manager

> Note: advanced settings for `Proxy Host` is required.

```
location / {
    proxy_set_header   X-Forwarded-For $remote_addr;
    proxy_set_header   Host $http_host;
    proxy_pass         "http://$server:$port";
    proxy_http_version 1.1;
    proxy_set_header   Upgrade $http_upgrade;
    proxy_set_header   Connection "upgrade";
}
```