# Matsuri Monitor

Monitors livestream chat from Hololive + Holostars streams and records messages that contain certain keywords or written by certain users.

Blatantly uses [dragonjet's](https://twitter.com/dragonjetmkii) JSON endpoints from his [Hololive Tools](https://hololive.jetri.co/#/) site to monitor live streams.

Named "Matsuri Monitor" because I'm obsessed and that's how I plan to use it, but can be customized to monitor any regex or username by modifying the `groupers.json` file.

Code sucks but is probably functional.

You can (probably) deploy it yourself by doing this, replacing `$LOCAL_PORT` with the port on your local machine to serve from and `$LOCAL_ARCHIVES_DIR` with the directory on your local machine to save gzipped JSON reports to.

```bash
$ docker build -t matsuri-monitor .
$ docker run -d \
    --name matsuri-monitor \
    -p 127.0.0.1:$LOCAL_PORT:8080/tcp \
    --mount type=bind,target=/app/archives,source=$LOCAL_ARCHIVES_DIR \
    matsuri-monitor
```
