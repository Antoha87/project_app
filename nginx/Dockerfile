FROM nginx:latest
WORKDIR /app
COPY /nginx /app
RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx/default.conf /etc/nginx/conf.d/default.conf