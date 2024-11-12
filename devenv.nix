{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  # env.GREET = "devenv";

  # https://devenv.sh/packages/
  # packages = [ pkgs.git ];

  # https://devenv.sh/languages/
  languages.rust.enable = true;
  languages.python = {
    enable = true;
    version = "3.11.3";

    venv = {
      enable = true;
      requirements = ./requirements.txt;
    };
  };
  cachix.enable = false;

  # https://devenv.sh/processes/
  # processes.cargo-watch.exec = "cargo-watch";

  # https://devenv.sh/services/
  services.postgres = {
    enable = true;
    createDatabase = true;
    package = pkgs.postgresql_15;
    initialDatabases = [{ 
      name = "mydb";
      schema = ./mydb.sql;
      pass = "testing";
      user = "rose";}];

    listen_addresses = "127.0.0.1"; 
    initialScript = "CREATE DATABASE mydb";
    
    extensions = extensions: [
      extensions.pg_cron
      extensions.postgis
      extensions.timescaledb
    ];
  };

  # https://devenv.sh/scripts/
  # scripts.hello.exec = ''
  #   echo hello from $GREET
  # '';

  # enterShell = ''
  #   hello
  #   git --version
  # '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  # enterTest = ''
  #   echo "Running tests"
  #   git --version | grep --color=auto "${pkgs.git.version}"
  # '';

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
