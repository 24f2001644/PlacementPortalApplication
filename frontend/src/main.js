import { createApp } from "vue"

import { createPinia } from "pinia"

import App from "./App.vue"

import router from "./router"

import "bootstrap/dist/css/bootstrap.min.css"

import "bootstrap/dist/js/bootstrap.bundle.min.js"

import "bootstrap-icons/font/bootstrap-icons.css"

import "./assets/admin.css"

createApp(App)

.use(createPinia())

.use(router)

.mount("#app")