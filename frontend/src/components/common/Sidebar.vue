<template>

<div
    class="bg-dark text-white vh-100 p-3"
    style="width:250px;">

    <h4 class="mb-4">

        Dashboard

    </h4>

    <ul class="nav flex-column">

        <li
            class="nav-item mb-2"
            v-for="item in menu"
            :key="item.path">

            <router-link
                :to="item.path"
                class="nav-link text-white">

                <i
                    :class="item.icon"
                    class="me-2">

                </i>

                {{ item.title }}

            </router-link>

        </li>

    </ul>

</div>

</template>

<script setup>

import { computed } from "vue";

import { useAuthStore } from "../../stores/auth";

const authStore = useAuthStore();

const menu = computed(() => {

    switch(authStore.role){

        case "ADMIN":

            return [

                {

                    title:"Dashboard",

                    path:"/admin/dashboard",

                    icon:"bi bi-speedometer2"

                },

                {

                    title:"Companies",

                    path:"/admin/companies",

                    icon:"bi bi-building"

                },

                {

                    title:"Students",

                    path:"/admin/students",

                    icon:"bi bi-people"

                },

                {

                    title:"Drives",

                    path:"/admin/drives",

                    icon:"bi bi-calendar-event"

                },

                {

                    title:"Applications",

                    path:"/admin/applications",

                    icon:"bi bi-file-earmark-text"

                },

                {

                    title:"Statistics",

                    path:"/admin/statistics",

                    icon:"bi bi-bar-chart"

                }

            ];

        case "COMPANY":

            return [

                {

                    title:"Dashboard",

                    path:"/company/dashboard",

                    icon:"bi bi-speedometer"

                },

                {

                    title:"Profile",

                    path:"/company/profile",

                    icon:"bi bi-person"

                },

                {

                    title:"Create Drive",

                    path:"/company/create-drive",

                    icon:"bi bi-plus-circle"

                },

                {

                    title:"Manage Drives",

                    path:"/company/drives",

                    icon:"bi bi-calendar"

                },

                {

                    title:"Applicants",

                    path:"/company/applicants",

                    icon:"bi bi-people"

                }

            ];

        default:

            return [

                {

                    title:"Dashboard",

                    path:"/student/dashboard",

                    icon:"bi bi-speedometer"

                },

                {

                    title:"Profile",

                    path:"/student/profile",

                    icon:"bi bi-person"

                },

                {

                    title:"Placement Drives",

                    path:"/student/drives",

                    icon:"bi bi-briefcase"

                },

                {

                    title:"Applications",

                    path:"/student/applications",

                    icon:"bi bi-file-earmark"

                },

                {

                    title:"History",

                    path:"/student/history",

                    icon:"bi bi-clock-history"

                }

            ];

    }

});

</script>

<style scoped>

.nav-link{

    border-radius:8px;

}

.nav-link:hover{

    background:#0d6efd;

}

</style>