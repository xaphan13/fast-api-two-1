#!/bin/bash


#**************************************************************************************
#*****************************************************************  rm-on-exit
declare -a files_to_be_deleted

function rm-on-exit() {
	[[ $# -gt 0 ]] && files_to_be_deleted+=("$@")
}

function on-exit() {
	for file in "${files_to_be_deleted[@]:-}"; do
		[[ -f "$file" ]] && rm -r "$file"
	done
	files_to_be_deleted=()
}

trap on-exit EXIT INT TERM QUIT ABRT ERR
#*****************************************************************  rm-on-exit
#**************************************************************************************



#**************************************************************************************
#***************************************************************** for example - write file
after_rules="$HOME/222/file-test-origin.txt"
after_rules_tmp="$HOME/222/file-test-tmp.txt"
after_rules_result="$HOME/222/file-test-result.txt"

function cmd--file() {
	cp "$after_rules" "$after_rules_tmp"  # create temp file
	rm-on-exit "$after_rules_tmp"         # delete temp file

	#********************************************** delete OLD
	sed "/^BEGIN start/,/^END stop/d" "$after_rules" > "$after_rules_tmp"

	#********************************************** added block text
	>> "${after_rules_tmp}" cat <<-\EOF
	BEGIN start
	new first string
	new second string
	END stop
	EOF
	#********************************************** "EOF" end of block of text

	diff -u --color=auto "$after_rules" "$after_rules_tmp"
	cat "$after_rules_tmp" > "$after_rules_result"
}
#***************************************************************** for example - write file


#***************************************************************** for example
function cmd--start() {
	declare service_action="${1:-help}"
	case "$service_action" in
	start)
		execute_command "docker stop redis_new"
		;;
	*)
		execute_command "docker stop pgadmin_new"
		;;
esac
}
#***************************************************************** for example
#**************************************************************************************
#**************************************************************************************









#***********************************************************************
# Функция для выполнения команды с выводом результата
#-----------------------------------------------------------------------
execute_command() {
    local command="$1"
    echo "--------------------------------------------------"
    echo "$ $command"
    eval "$command"
    local exit_code=$?
    if [ $exit_code -eq 0 ]; then
        echo "--------------------------------------------------"
    else
        echo "Command failed with exit code $exit_code"
    fi
}
#***********************************************************************



#***********************************************************************
function cmd--help() {
	cat <<-EOF >&2
	Examples:
	  cmd br == git branch -a

	  cmd st == git status
	EOF
}
#***********************************************************************



#***********************************************************************
# __main__
#-----------------------------------------------------------------------
cmd_action="${1:-}"


case "$cmd_action" in
  br)
	  execute_command "git branch -a"
		;;
	st)
	  execute_command "git status"
		;;
  file)
		cmd--file
		;;
	*)
		cmd--help
		;;
esac
#***********************************************************************
