import PageLayout from '../../components/PageLayout'
import WrapperFirstBlock from '../../components/WrapperFirstBlock'

import Intro from '../_CommonBlocks/Intro'
import Block1 from './Block1'
import Block2 from './Block2'
import HappyClients from '../_CommonBlocks/HappyClients'
import CallForm from '../_CommonBlocks/CallForm'
import ContactForm from '../_CommonBlocks/ContactForm'

import illustration from '../../assets/components/treatmentdetail-introillustration.jpg'
import {useTranslation} from "react-i18next";

export default function Page()
{
    const {t} = useTranslation();
    return <PageLayout
        title={t("page_training_title")}
    >
        <WrapperFirstBlock>
            <Intro
                title={t('page_training_title')}
                illustration={illustration}
            />
        </WrapperFirstBlock>
        <Block1/>
        <Block2/>
        <HappyClients/>
        <CallForm/>
        <ContactForm/>
    </PageLayout>
}