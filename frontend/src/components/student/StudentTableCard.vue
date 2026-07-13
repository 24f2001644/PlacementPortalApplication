<template>


<div class="table-card">


    <!-- Header -->


    <div class="table-header">


        <h5>

            {{ title }}

        </h5>



        <div v-if="$slots.actions">

            <slot name="actions"></slot>

        </div>


    </div>




    <!-- Table Content -->


    <div class="table-body">


        <slot></slot>


    </div>



</div>


</template>



<script setup>


defineProps({


    title:{


        type:String,

        required:true


    }


})


</script>

<style scoped>


.table-card{


    background:white;

    border-radius:18px;

    box-shadow:0 8px 24px rgba(0,0,0,.05);

    overflow:hidden;

    margin-bottom:25px;


}



.table-header{


    padding:18px 25px;

    display:flex;

    justify-content:space-between;

    align-items:center;

    background:#F8FAFC;

    border-bottom:1px solid #E2E8F0;


}



.table-header h5{


    margin:0;

    font-size:18px;

    font-weight:700;

    color:#0F172A;


}



.table-body{


    padding:20px;

    overflow-x:auto;


}



.table{


    margin-bottom:0;


}



.table thead{


    background:#F1F5F9;


}



.table th{


    color:#475569;

    font-weight:600;

    white-space:nowrap;


}



.table td{


    vertical-align:middle;

    color:#334155;


}



.table tbody tr:hover{


    background:#F8FAFC;


}



@media(max-width:768px){


    .table-header{


        padding:15px 18px;


    }



    .table-body{


        padding:15px;


    }


}


</style>