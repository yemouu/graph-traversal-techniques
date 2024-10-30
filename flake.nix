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
            hatch
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
        graph-traversal = final.callPackage ./nix/packages { };
      };

      packages = forAllSystems (pkgs: rec {
        default = graph-traversal;
        graph-traversal= pkgs.graph-traversal;
      });

      apps = forAllSystems (pkgs: rec {
        default = graph-traversal;
        graph-traversal= {
          type = "app";
          program = "${pkgs.graph-traversal}/bin/graph-traversal";
        };
      });
    };
}
