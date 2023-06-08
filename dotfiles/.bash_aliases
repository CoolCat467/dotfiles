### EXPORTS ###
# export PS1='\[\033[01;34m\]\w \[\033[00m\]> ' # Noncolor
export PS1='\[\033[01;34m\]\w \[\033[00m\]> ' # New

# export PATH="$HOME/.local/bin:$PATH"
# export PATH="$HOME/.bin:$PATH"
# export PATH="$HOME/.cargo/bin:$PATH"
export MYPYPATH="$HOME/.idlerc/mypy/stubs"
export MYPY_CACHE_DIR="$HOME/.idlerc/mypy"


### OTHER ###
xhost local:$USER > /dev/null


# ### LINUXBREW ###
# BREWD=0
# alias brew='[[ $BREWD == '0' ]] && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv) && BREWD=1; brew '


### Python ###
alias python3='/usr/bin/python3.11'
alias pip='/usr/bin/python3.11 -m pip '


### TMUX ###
alias tm='tmux '
alias tma='tmux attach -t $1'
alias tmx='tmux kill-session -t $1'
alias tmls='tmux list-sessions'


### ALIASES ###
alias profile='nano ~/.bash_aliases'
alias c='clear'
alias rf='source ~/.bashrc'
alias x='exit'
alias rc='clear;rf;cd ~'
alias ding='s=$(ifconfig | grep 'broadcast'); a="${s[@]:6}"; : $(ping -qc 5 "$a"); arp -a'
alias apt-get='sudo apt-get '
alias m='alpine'
alias root='sudo -s'
alias apscan='sudo arp-scan -l'
alias s='lynx duckduckgo.com'
alias killall='kill -9 -1'
alias fix='dos2unix '
alias fxbin='cd .bin; chmod 755 *; dos2unix *; rc'
alias ha='hangups --col-scheme solarized-dark'
alias fxdir='chmod 755 *; dos2unix *'
alias octperm='stat -c '%a' '
alias screenshot='scrot -d 10'
alias send='woof -p 8080 -c 1 -z $1'
#alias dlmusic='youtube-dl -x --audio-format mp3 '
alias dlmusic='yt-dlp -x --audio-format mp3 --audio-quality 0 '
alias cdNetworkPasswords='cd /etc/NetworkManager/system-connections/'
alias sublime='sublime-text.subl'
alias whatos='cat /etc/os-release'
#alias whatdev='cat /proc/device-tree/model'

### AUTO-RUN ###
# hello
python3.11 ~/.bin/hello
