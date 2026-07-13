<template>

<div class="admin-sidebar">

    <div class="logo">

        <i class="bi bi-mortarboard-fill"></i>

        <span>Placement Portal</span>

    </div>

    <div class="menu">

        <router-link
            v-for="item in menu"
            :key="item.name"
            :to="item.route"
            class="menu-item"
            active-class="active-link"
        >

            <i :class="item.icon"></i>

            <span>{{ item.name }}</span>

        </router-link>

    </div>

    <div class="logout">

        <button
            class="btn btn-danger w-100"
            @click="logout"
        >

            <i class="bi bi-box-arrow-right me-2"></i>

            Logout

        </button>

    </div>

</div>

</template>

<script setup>

import { useRouter } from "vue-router"
import { useAuthStore } from "../../stores/auth"

const router = useRouter()

const auth = useAuthStore()

const menu = [

{
name:"Dashboard",
route:"/admin/dashboard",
icon:"bi bi-speedometer2"
},

{
name:"Companies",
route:"/admin/companies",
icon:"bi bi-buildings"
},

{
name:"Students",
route:"/admin/students",
icon:"bi bi-people"
},

{
name:"Placement Drives",
route:"/admin/drives",
icon:"bi bi-briefcase"
},

{
name:"Applications",
route:"/admin/applications",
icon:"bi bi-file-earmark-text"
},

{
name:"Statistics",
route:"/admin/statistics",
icon:"bi bi-bar-chart-line"
}

]

function logout(){

auth.logout()

router.push("/login")

}

</script>

<style scoped>

.admin-sidebar{

width:270px;

min-height:100vh;

background:#1E293B;

display:flex;

flex-direction:column;

padding:25px;

color:white;

position:sticky;

top:0;

}

.logo{

display:flex;

align-items:center;

gap:12px;

font-size:22px;

font-weight:700;

margin-bottom:40px;

}

.logo i{

font-size:28px;

color:#818CF8;

}

.menu{

display:flex;

flex-direction:column;

gap:10px;

}

.menu-item{

display:flex;

align-items:center;

gap:14px;

padding:14px 18px;

border-radius:14px;

color:#CBD5E1;

transition:.25s;

font-weight:500;

}

.menu-item:hover{

background:#334155;

color:white;

}

.active-link{

background:#4F46E5;

color:white;

}

.logout{

margin-top:auto;

}

</style>