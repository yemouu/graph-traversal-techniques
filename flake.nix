{
  description = "Algorithm Analysis group project on graph traversal techniques";

  inputs.nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      forAllSystems = function: nixpkgs.lib.genAttrs [ "x86_64-linux" ]
        (system: function (import nixpkgs {
          inherit system;
          overlays = [ self.overlays.default ];
        }));
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            ruff
            (with python3Packages; [
              build
              hatchling
            ])
          ];
        };
      });

      overlays.default = final: prev: {
        graph-traversal-driver = final.callPackage ./nix/packages { };
      };

      packages = forAllSystems (pkgs: rec {
        default = graph-traversal-driver;
        graph-traversal-driver = pkgs.graph-traversal-driver;
      });

      apps = forAllSystems (pkgs: rec {
        default = graph-traversal-driver;
        graph-traversal-driver = {
          type = "app";
          program = "${pkgs.graph-traversal-driver}/bin/graph-traversal-driver";
        };
      });
    };
}
