import PageLayout from '../../components/PageLayout'

import Block1 from './Block1'
import Block2 from './Block2'
import Block3 from './Block3'
import Block4 from './Block4'

import WhyShouldYouContact from '../_CommonBlocks/WhyShouldYouContact'
import ContactForm from '../_CommonBlocks/ContactForm'
import CallForm from '../_CommonBlocks/CallForm'
import HappyClients from '../_CommonBlocks/HappyClients'
import {useEffect} from "react";

export default function Page(){

    useEffect(() => { //jivochat
        const script = document.createElement('script');
        script.src = "//code.jivosite.com/widget/E0EaxnNlBr";
        script.async = true;
        document.body.appendChild(script);

        return () => {
            script.remove(); // Функция очистки для удаления скрипта при unmount
        };
    }, []);

    return(
        <div>
            <PageLayout>
                <Block1/>
                <Block2/>
                <Block3/>
                <Block4/>
                <WhyShouldYouContact/>
                <HappyClients/>
                <CallForm/>
                <ContactForm/>
            </PageLayout>
        </div>
)}
