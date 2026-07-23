<template>


<div class="student-navbar">


    <!-- Welcome Section -->

    <div class="welcome">


        <h3>

            Welcome Back 👋

        </h3>


        <small>

            Track your placement journey here.

        </small>


    </div>




    <!-- Right Section -->


    <div class="right-section">



        <!-- Search -->


        <div class="search-box">


            <i class="bi bi-search"></i>


            <input

                type="text"

                placeholder="Search..."

            />


        </div>




        <!-- Notification -->


        <button

            class="icon-btn"

        >

            <router-link
                to="/student/notifications"
                class="icon-btn"
            >
                <i class="bi bi-bell"></i>
            </router-link>


        </button>






        <!-- Profile -->


        <div class="profile">


            <div class="avatar">

                {{ initial }}

            </div>



            <div>


                <strong>

                    {{ studentName }}

                </strong>


                <br>


                <small>

                    Student

                </small>


            </div>


        </div>



    </div>



</div>


</template>



<script setup>


import { computed } from "vue"

import { useRouter } from "vue-router"

import { useAuthStore } from "../../stores/auth"



const router = useRouter()


const auth = useAuthStore()



const studentName = computed(()=>{


    return auth.user?.name || "Student"


})



const initial = computed(()=>{


    return studentName.value.charAt(0).toUpperCase()


})




function openNotifications(){


    router.push("/student/notifications")


}



</script>

<style scoped>


.student-navbar{


    background:white;

    padding:20px 30px;

    display:flex;

    justify-content:space-between;

    align-items:center;

    border-radius:18px;

    box-shadow:0 8px 24px rgba(0,0,0,.05);

    margin-bottom:30px;


}



.welcome h3{


    margin:0;

    font-weight:700;


}



.welcome small{


    color:#64748B;


}




.right-section{


    display:flex;

    align-items:center;

    gap:20px;


}




.search-box{


    display:flex;

    align-items:center;

    background:#F1F5F9;

    padding:10px 18px;

    border-radius:14px;

    width:280px;


}



.search-box i{


    color:#64748B;


}



.search-box input{


    border:none;

    background:none;

    outline:none;

    width:100%;

    margin-left:10px;


}




.icon-btn{


    width:46px;

    height:46px;

    border:none;

    background:#E0F2FE;

    border-radius:50%;

    font-size:20px;

    color:#0284C7;

    transition:.25s;


}



.icon-btn:hover{


    background:#0284C7;

    color:white;


}




.profile{


    display:flex;

    align-items:center;

    gap:14px;


}



.profile small{


    color:#64748B;


}



.avatar{


    width:48px;

    height:48px;

    border-radius:50%;

    background:#0284C7;

    display:flex;

    align-items:center;

    justify-content:center;

    color:white;

    font-size:20px;

    font-weight:700;


}




@media(max-width:768px){


    .student-navbar{


        flex-direction:column;

        gap:20px;

        align-items:flex-start;


    }



    .right-section{


        width:100%;

        flex-wrap:wrap;


    }



    .search-box{


        width:100%;


    }


}


</style>

