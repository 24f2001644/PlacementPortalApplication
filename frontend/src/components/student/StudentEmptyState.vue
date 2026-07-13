<template>


<div class="empty-state">


    <div class="empty-icon">


        <i :class="icon"></i>


    </div>



    <h5>

        {{ title }}

    </h5>



    <p>

        {{ message }}

    </p>



</div>


</template>



<script setup>


defineProps({


    title:{


        type:String,

        default:"No Data Found"


    },



    message:{


        type:String,

        default:"There is nothing to display here."


    },



    icon:{


        type:String,

        default:"bi bi-inbox"


    }


})


</script>

<style scoped>


.empty-state{


    text-align:center;

    padding:40px 20px;

    color:#64748B;


}



.empty-icon{


    width:70px;

    height:70px;

    border-radius:50%;

    background:#E0F2FE;

    display:flex;

    align-items:center;

    justify-content:center;

    margin:0 auto 20px;


}



.empty-icon i{


    font-size:32px;

    color:#0284C7;


}



h5{


    font-weight:700;

    color:#0F172A;

    margin-bottom:8px;


}



p{


    margin:0;

    font-size:15px;


}


</style>