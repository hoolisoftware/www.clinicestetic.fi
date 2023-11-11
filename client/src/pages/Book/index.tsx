import PageLayout from '../../components/PageLayout'

import WrapperFirstBlock from '../../components/WrapperFirstBlock'

import Block from './Block'
import {useTranslation} from "react-i18next";


export default function Page()
{
    const {t} = useTranslation();
    return <PageLayout
        title={t("page_book_title")}
    >
        <WrapperFirstBlock>
            <Block/>
        </WrapperFirstBlock>
    </PageLayout>
}