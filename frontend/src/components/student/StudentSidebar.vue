<template>

<div class="student-sidebar">


    <!-- Logo -->

    <div class="logo">

        <i class="bi bi-mortarboard-fill"></i>

        <span>Placement Portal</span>

    </div>



    <!-- Menu -->

    <div class="menu">


        <router-link

            v-for="item in menu"

            :key="item.name"

            :to="item.route"

            class="menu-item"

            active-class="active-link"

        >


            <i :class="item.icon"></i>


            <span>

                {{ item.name }}

            </span>


        </router-link>



    </div>



    <!-- Logout -->


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

    route:"/student/dashboard",

    icon:"bi bi-speedometer2"

},

{

    name:"Profile",

    route:"/student/profile",

    icon:"bi bi-person-circle"

},

{

    name:"Placement Drives",

    route:"/student/drives",

    icon:"bi bi-briefcase-fill"

},

{

    name:"Applications",

    route:"/student/applications",

    icon:"bi bi-file-earmark-text"

},

{

    name:"History",

    route:"/student/history",

    icon:"bi bi-clock-history"

},

{

    name:"Export Applications",

    route:"/student/export",

    icon:"bi bi-download"

}

]



function logout(){


    auth.logout()


    router.push("/login")


}


</script>

<style scoped>


.student-sidebar{


    width:270px;

    min-height:100vh;

    background:#0F172A;

    display:flex;

    flex-direction:column;

    padding:25px;

    color:white;

    position:sticky;

    top:0;

    flex-shrink:0;

    box-sizing:border-box;


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

    color:#38BDF8;


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



.menu-item i{


    font-size:18px;


}



.menu-item:hover{


    background:#1E293B;

    color:white;


}



.active-link{


    background:#0284C7;

    color:white;


}



.logout{


    margin-top:auto;


}



.logout button{


    border-radius:12px;

    padding:12px;


}



@media(max-width:768px){


    .student-sidebar{


        width:100%;

        min-height:auto;

        position:relative;


    }


}



</style>