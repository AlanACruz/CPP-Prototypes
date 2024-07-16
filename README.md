# CPP-Prototypes

# Git Clone
```
git clone git@github.com:AlanACruz/CPP-Prototypes.git ~/git/CPP-Prototypes
```

# Install Docker on Chromebook
https://github.com/AlanACruz/DevSecOps/blob/master/docker/Install-Docker-On-Chromebook.md

# Conan Container
```
docker pull conanio/gcc11
```

# Run Container
## TODO Upgrade to Conan 2
## https://docs.conan.io/2/examples/runners/docker/basic.html
```
docker run
    -v ~/.nuget:/root/.nuget/
    -v ~/git/CPP-Prototypes:/home/conan/git/CPP-Prototypes
    -t
    -i
    --rm
    conanio/gcc11
```