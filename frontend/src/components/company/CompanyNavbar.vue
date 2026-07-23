<template>

<div class="navbar-card">

    <div>

        <h3>

            Welcome Recruiter 👋

        </h3>

        <small>

            Manage placement drives and recruit talented students.

        </small>

    </div>



    <div class="right">

        <div class="search">

            <i class="bi bi-search"></i>

            <input

                type="text"

                placeholder="Search..."

            >

        </div>



        <button

            class="icon-btn"

        >

            <router-link to="/company/notifications">

                <i class="bi bi-bell"></i>

            </router-link>

        </button>



        <div class="profile">

            <div class="avatar">

                C

            </div>

            <div>

                <strong>

                    Company

                </strong>

                <br>

                <small>

                    Recruiter

                </small>

            </div>

        </div>

    </div>

</div>

</template>

<style scoped>

.navbar-card{

background:white;

padding:20px 30px;

display:flex;

justify-content:space-between;

align-items:center;

border-radius:18px;

box-shadow:0 8px 24px rgba(0,0,0,.05);

margin-bottom:30px;

}



.right{

display:flex;

align-items:center;

gap:20px;

}



.search{

display:flex;

align-items:center;

background:#F1F5F9;

padding:10px 18px;

border-radius:14px;

width:280px;

}



.search input{

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

background:#DCFCE7;

border-radius:50%;

font-size:20px;

color:#16A34A;

transition:.25s;

}



.icon-btn:hover{

background:#16A34A;

color:white;

}



.profile{

display:flex;

align-items:center;

gap:14px;

}



.avatar{

width:48px;

height:48px;

border-radius:50%;

background:#16A34A;

display:flex;

align-items:center;

justify-content:center;

font-size:20px;

font-weight:700;

color:white;

}



@media(max-width:768px){

.navbar-card{

flex-direction:column;

gap:20px;

align-items:flex-start;

}



.right{

width:100%;

justify-content:space-between;

}



.search{

width:100%;

}

}

</style>