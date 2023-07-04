#/usr/bin/sh -x
docker buildx build --platform linux/amd64 -t deploy_while_build_just_remove_this_after_build .