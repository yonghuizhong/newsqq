#!/bin/sh
mongo newsQQDB --eval "show collections;db.links.find({},{article:0,_id:0,introduce:0}).limit(3);"