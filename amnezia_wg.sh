#!/bin/bash

set -o errexit

CFG_PATH="/path/to/cfg/config.conf"
AWG_INTERFACE=$(basename "$CFG_PATH" .conf)


function amnezia_status() {
	if ip a show "$AWG_INTERFACE" &> /dev/null; then
		return 0
	else
		return 1
	fi
}

function print_amnezia_status() {
	if amnezia_status; then
		echo ""
	else echo ""
	fi
}

function amnezia_toggle() {
	if [ "$1" == "status" ]; then
		sleep 0.2
		print_amnezia_status
	else
		if amnezia_status; then
			awg-quick down "$CFG_PATH" &> /dev/null
		else
			awg-quick up "$CFG_PATH" &> /dev/null
		fi
		sleep 0.2
		print_amnezia_status
	fi

}

amnezia_toggle "$@"