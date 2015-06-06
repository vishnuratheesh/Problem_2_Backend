#!/bin/bash

LOCAL_DATABASE_URL="postgres://user:password@localhost:5432/mydbname"

function deinit_env {
unset DATABASE_URL
deactivate
}

function use_remote_db {
DATABASE_URL=$(heroku config | grep DATABASE_URL)
DATABASE_URL=${DATABASE_URL#*:*postgres:}
DATABASE_URL="postgres:"$DATABASE_URL
export DATABASE_URL
echo "Now using remote database at: "$DATABASE_URL
}

function use_local_db {
DATABASE_URL=$LOCAL_DATABASE_URL
export DATABASE_URL
echo "Now using local database at: "$DATABASE_URL
}

source env/bin/activate
use_remote_db

