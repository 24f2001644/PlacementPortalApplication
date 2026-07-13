<template>


<div class="page-header">


    <div>


        <h2>

            {{ title }}

        </h2>


        <p>

            {{ subtitle }}

        </p>


    </div>



    <div v-if="showButton">


        <button

            class="btn btn-primary"

            @click="$emit('action')"

        >

            <i

                v-if="icon"

                :class="icon"

            ></i>


            {{ buttonText }}


        </button>


    </div>



</div>


</template>



<script setup>


defineProps({


    title:{


        type:String,

        required:true


    },



    subtitle:{


        type:String,

        default:""


    },



    showButton:{


        type:Boolean,

        default:false


    },



    buttonText:{


        type:String,

        default:""


    },



    icon:{


        type:String,

        default:""


    }



})



defineEmits([

    "action"

])


</script>

<style scoped>


.page-header{


    background:white;

    padding:25px 30px;

    border-radius:18px;

    display:flex;

    justify-content:space-between;

    align-items:center;

    box-shadow:0 8px 24px rgba(0,0,0,.05);

    margin-bottom:30px;


}



.page-header h2{


    margin:0;

    font-size:28px;

    font-weight:700;

    color:#0F172A;


}



.page-header p{


    margin:8px 0 0;

    color:#64748B;

    font-size:15px;


}



.btn-primary{


    background:#0284C7;

    border:none;

    padding:12px 20px;

    border-radius:12px;

    font-weight:600;


}



.btn-primary:hover{


    background:#0369A1;


}



.btn-primary i{


    margin-right:8px;


}



@media(max-width:768px){


    .page-header{


        flex-direction:column;

        align-items:flex-start;

        gap:20px;


    }


}


</style>