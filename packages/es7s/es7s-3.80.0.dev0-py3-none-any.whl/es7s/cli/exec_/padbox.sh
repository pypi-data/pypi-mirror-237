#!/bin/bash
#-------------------------------------------------------------------------------
# es7s/core
# (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
#-------------------------------------------------------------------------------
# shellcheck disable=SC2153,SC2209,SC2059,SC2086

function _help {
  cat <<EOF

    Execute the command and pad the output. Suggested usage is as
    a helper for making consistent terminal screenshots which are
    easy to crop.

USAGE
    padbox [COMMAND [ARGS...]]

DESCRIPTION
    When launched with at least one argument: execute the COMMAND
    with ARGS, and return the output padded with an empty line(s)
    and spaces. Also prepend the output with the COMMAND and ARGS
    as if they were typed in manually.

    When launched without arguments: read standard input, process
    it as described above, except that a line with the COMMAND is
    omitted from the output.

ENVIRONMENT
    ES7S_PADBOX_HEADER
        Display specified string instead of COMMAND ARGS... .
    ES7S_PADBOX_NO_HEADER
        Non-empty value disables displaying COMMAND ARGS... line.
    ES7S_PADBOX_NO_CLEAR
        Non-empty value disables preliminary screen clearing.
    ES7S_PADBOX_PAD_X
        Add specified number of spaces to the left and right [3].
    ES7S_PADBOX_PAD_Y
        Add specified number of empty lines above and below [1].

    Numbers in square brackets indicate the default values.

EXAMPLES
    padbox git status
    git status | padbox
EOF
}

function _main {
  local pager="$PAGER"
  [[ "$pager" =~ less ]] && pager="$pager -RS"
  command -v "${pager:-""}" &>/dev/null || pager=cat

  [[ -z $ES7S_PADBOX_NO_CLEAR ]] && PS1="> " && clear
  unset PROPMT_COMMAND

  local header="> ${ES7S_PADBOX_HEADER:-$*}\n\n"
  [[ -n $ES7S_PADBOX_NO_HEADER ]] && header=

  local pad_x="$(printf %${ES7S_PADBOX_PAD_X:-3}s)"

  (
    _pad_y
    [[ $# -eq 0 ]] && set "cat"
    printf "$header"
    COLUMNS=$(($(tput cols) - 6)) "$@" 2>&1
    _pad_y
  ) | sed -e "/\S/ s/^/$pad_x/" |
    $pager
}
function _pad_y {
  printf "%${ES7S_PADBOX_PAD_Y:-1}s" | tr ' ' $'\n'
}

[[ $# -gt 1 ]] || [[ $* =~ (--)?help ]] && _help && exit
_main "$@"
