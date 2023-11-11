import PageLayout from '../../components/PageLayout'
import WrapperFirstBlock from '../../components/WrapperFirstBlock'

import Block1 from './Block1'
import {useTranslation} from "react-i18next";


export default function Page() {
    const {t} = useTranslation();
    return <PageLayout
        title={t('page_news_title')}
    >
        <WrapperFirstBlock>
            <Block1/>
        </WrapperFirstBlock>
    </PageLayout>
}