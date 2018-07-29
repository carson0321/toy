#!/bin/sh
#########################################################################
# File Name: clone-all-project.sh
# Author: Carson Wang
# mail: r03944040@g.ntu.edu.tw
# Created Time: 2018-07-09 17:35:29
#########################################################################

BLACK="\033[0;30m" RED="\033[0;31m" GREEN="\033[0;32m" ORANGE="\033[0;33m" BLUE="\033[0;34m" PURPLE="\033[0;35m" CYAN="\033[0;36m" LIGHT_GRAY="\033[0;37m" DARK_GRAY="\033[1;30m" LIGHT_RED="\033[1;31m" LIGHT_GREEN="\033[1;32m" YELLOW="\033[1;33m" LIGHT_BLUE="\033[1;34m" LIGHT_PURPLE="\033[1;35m" LIGHT_CYAN="\033[1;36m" WHITE="\033[1;37m" NC="\033[0m"

TOKEN=""
GITLAB_URL=""

if [[ $1 == "clone" ]]; then
    PREFIX="ssh_url_to_repo"
    curl --header "PRIVATE-TOKEN: $TOKEN" $GITLAB_URL/api/v3/projects | grep -o "\"$PREFIX\":[^ ,]\+" | awk -F 'ssh://' '{printf "\"ssh://"; for (i=2; i<NF; i++) printf $i ; print $NF}' | xargs -L1 git clone
elif [[ $1 == "pull" ]]; then
    for d in ./*/ ; do
        (cd "$d" && git pull);
    done
else
    echo "${RED}Error parameter${NC}"
fi
