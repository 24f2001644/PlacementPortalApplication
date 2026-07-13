<template>

<div class="company-sidebar">

    <div class="logo">

        <i class="bi bi-building-fill"></i>

        <span>Company Portal</span>

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

route:"/company/dashboard",

icon:"bi bi-speedometer2"

},

{

name:"Profile",

route:"/company/profile",

icon:"bi bi-person-badge"

},

{

name:"Create Drive",

route:"/company/create-drive",

icon:"bi bi-plus-circle"

},

{

name:"Manage Drives",

route:"/company/drives",

icon:"bi bi-briefcase"

},

{

name:"Applications",

route:"/company/drives/1/applications",

icon:"bi bi-file-earmark-text"

},

{

name:"Selected",

route:"/company/selected",

icon:"bi bi-award"

}

]

function logout(){

    auth.logout()

    router.push("/login")

}

</script>

<style scoped>

.company-sidebar{

width:270px;

min-height:100vh;

background:#0F172A;

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

color:#22C55E;

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

text-decoration:none;

transition:.25s;

font-weight:500;

}

.menu-item:hover{

background:#1E293B;

color:white;

}

.active-link{

background:#16A34A;

color:white;

}

.logout{

margin-top:auto;

}

</style>