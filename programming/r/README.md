how to use R studio in docker: https://github.com/rocker-org/rocker/wiki/Using-the-RStudio-image

summary:

pull rstudio: *docker pull rocker/rstudio*

run rstudio: *docker run -p 8787:8787 -v /home/rid/RStudio:/home/rstudio rocker/rstudio (the login user is rstudio)*

where -v is to link up the host volume (a folder) with the container's path

after running rstudio, users can access files at /home/rid/RStudio directly.
