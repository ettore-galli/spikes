# VIM


## CONFIGURAZIONE VIM

~/.vimrc

```
set number
```

## PLUGIN

### Siti interessanti

Tutorial vim come IDE
https://www.linuxfordevices.com/tutorials/linux/turn-vim-into-an-ide

Comandi vim
https://stackoverflow.com/questions/5400806/what-are-the-most-used-vim-commands-keypresses/5400978#5400978

Sistema di plugin vim 8+
https://medium.com/@paulodiovani/installing-vim-8-plugins-with-the-native-pack-system-39b71c351fea
https://github.com/paulodiovani/dot-files/tree/main/home/user

### Procedura setup plugin

````bash

# Una Tantum

# Cartella generale
mkdir -p ~/.vim/pack

# La cartella è un repo git per usare i sottomoduli
cd ~/.vim/pack
git init

# Organizzazione della cartella in plugin
# start: plugin avviati a startup
# opt: plugin da avviare a comando

mkdir -p plugins/start
mkdir -p plugins/opt
mkdir -p themes/start
mkdir -p themes/opt

# Per ciascun plugin
git submodule add [repo git plugin] [cartella di destinazione]

# Airline

  git submodule add https://github.com/vim-airline/vim-airline plugins/start/vim-airline

  .vimrc:
  let g:airline#extensions#tabline#enabled = 1

  Da vim:
  :heltpags ~/.vim/pack/plugins/start/vim-airline/doc

# Fugitive (git)

  git submodule add https://github.com/tpope/vim-fugitive plugins/start/vim-fugitive

  Da vim:
  :helptags ~/.vim/pack/plugins/start/vim-fugitive/doc	

# The Nerd Tree

  git submodule add https://github.com/preservim/nerdtree

```

Elenco plugin:
https://vimawesome.com/

## Split windows
