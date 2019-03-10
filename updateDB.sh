#!/bin/bash
sql="db.links_backup.remove({});db.links_web.copyTo('links_backup');db.links_web.remove({});db.links.copyTo('links_web');"
echo $sql|/usr/bin/mongo 127.0.0.1:27017/newsQQDB --shell
