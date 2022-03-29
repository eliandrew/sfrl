# see https://josephsdavid.github.io/nix.html for a nice explanation
let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    name = "rlGymEnv";
    buildInputs = with pkgs; [
    # basic python dependencies
      python38Packages.numpy
      python38Packages.gym
      python38Packages.ipython
    ];
   shellHook = ''
   '';
  }

