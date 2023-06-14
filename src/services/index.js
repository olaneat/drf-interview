import axios from "axios";
import { Config } from "../env";

const createTask = (form) =>{ // api for creating task is created
    const url = `${Config.baseUrl}/create` // the url for created
    return axios.post(url, form) // the api is called passing in the neceray params
}


const taskList = () =>{ // the api for list all the task is created
    const url = `${Config.baseUrl}/list` // the url is created
    return axios.get(url) // the api is called passing in necerary params

}

const updateTask = (id, form) =>{ // api for updating task is created 
    const url = `${Config.baseUrl}/update/${id}` //url is created
    return axios.put(url, form) // the api is called

}
const deleteTask = (id) =>{ // delete api function is created
    const url = `${Config.baseUrl}/delete/${id}` // url is created
    return axios.delete(url) //delete api is called 

}

function getTaskById(id){
    const url = `${Config.baseUrl}/detail/${id}`
    return axios.get(url)
}



const  Services = { // the api obj containing all the functions is created
    createTask,
    updateTask,
    taskList,
    deleteTask,
    getTaskById

}


export default Services  //the OBJ is epported