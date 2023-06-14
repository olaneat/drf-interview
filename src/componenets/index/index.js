import React, {useState, useEffect} from "react";
import Style from  './index.module.css'
import { Link } from "react-router-dom";
import TaskList from "../list-tasks";
import AddIcon from '@mui/icons-material/Add';
const Index = () =>{
    

    return (
        <div className={`${Style.container} container` }>
            <h1 className={`${Style.header} row`}>Welcome </h1>
            <div className={`${Style.btn} row`}>
                <button className={` btn btn-primary col-sm-8 col-lg-4`} ><Link to={'/create-task'} className={`${Style.link}`}><AddIcon/>Create Task</Link> </button>
            </div>

                <h3>Tasks List</h3>
                <TaskList/>
        </div>
    )
}

export default Index