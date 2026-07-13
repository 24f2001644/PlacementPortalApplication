<template>


<div class="progress-card">


    <div class="header">


        <h5>

            {{ title }}

        </h5>


        <span>

            {{ value }}%

        </span>


    </div>



    <div class="progress">


        <div

            class="progress-bar"

            :style="{width:value+'%'}"

        >

        </div>


    </div>



    <p v-if="message">


        {{ message }}


    </p>



</div>


</template>



<script setup>


defineProps({


    title:{


        type:String,

        required:true


    },



    value:{


        type:Number,

        default:0


    },



    message:{


        type:String,

        default:""


    }


})


</script>

<style scoped>


.progress-card{


    background:white;

    padding:25px;

    border-radius:18px;

    box-shadow:0 8px 24px rgba(0,0,0,.05);

    margin-bottom:25px;


}



.header{


    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:18px;


}



.header h5{


    margin:0;

    font-size:18px;

    font-weight:700;

    color:#0F172A;


}



.header span{


    font-weight:700;

    color:#0284C7;

    font-size:18px;


}



.progress{


    height:12px;

    background:#E2E8F0;

    border-radius:20px;

    overflow:hidden;


}



.progress-bar{


    height:100%;

    background:#0284C7;

    border-radius:20px;

    transition:.4s;


}



p{


    margin:15px 0 0;

    color:#64748B;

    font-size:14px;


}




@media(max-width:768px){


    .progress-card{


        padding:18px;


    }


}


</style>