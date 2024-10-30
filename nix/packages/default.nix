{ pkgs, lib }:
pkgs.python3Packages.buildPythonApplication {
  pname = "graph-traversal-driver";
  version = "0.0.1";
  pyproject = true;

  src = ../../.;

  build-system = with pkgs.python3Packages; [ hatchling ];
  # dependencies = [ ];
  # nativeCheckInputs = [ ];

  meta = {
    description = "Algorithm Analysis group project on graph traversal techniques";
    homepage = "https://github.com/yemouu/graph-traversal-techniques";
    license = lib.licenses.bsd0;
  };
}
