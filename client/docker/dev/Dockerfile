FROM node:20.12.2

SHELL ["/bin/bash", "-c"]
WORKDIR "/client"

COPY package.json .

RUN apt update -q \
    && apt upgrade -qy \
    && npm i -g pnpm

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "-c", "pnpm i && pnpm dev"]
