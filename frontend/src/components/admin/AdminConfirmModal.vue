<script setup>

const props = defineProps({

    show: {
        type: Boolean,
        default: false
    },

    title: String,

    message: String,

    confirmText: {
        type: String,
        default: "Confirm"
    },

    confirmColor: {
        type: String,
        default: "danger"
    }

})

const emit = defineEmits([

    "confirm",

    "cancel"

])

</script>

<template>

<Transition name="fade">

<div

    v-if="show"

    class="modal-backdrop-custom"

>

    <div class="confirm-card">

        <h4>

            {{ title }}

        </h4>

        <p class="text-muted">

            {{ message }}

        </p>

        <div class="d-flex justify-content-end gap-2 mt-4">

            <button

                class="btn btn-light"

                @click="emit('cancel')"

            >

                Cancel

            </button>

            <button

                class="btn"

                :class="'btn-' + confirmColor"

                @click="emit('confirm')"

            >

                {{ confirmText }}

            </button>

        </div>

    </div>

</div>

</Transition>

</template>

<style scoped>

.modal-backdrop-custom{

    position:fixed;

    inset:0;

    background:rgba(15,23,42,.45);

    display:flex;

    justify-content:center;

    align-items:center;

    z-index:9999;

    backdrop-filter:blur(5px);

}

.confirm-card{

    background:white;

    width:450px;

    max-width:90%;

    padding:30px;

    border-radius:20px;

    box-shadow:0 25px 60px rgba(0,0,0,.18);

}

.fade-enter-active,

.fade-leave-active{

    transition:.25s ease;

}

.fade-enter-from,

.fade-leave-to{

    opacity:0;

    transform:scale(.9);

}

</style>