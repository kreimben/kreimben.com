import Layout from '../components/Layout'

import {loremIpsum} from '../components/loremipsum'

export default function Home() {
    return (
        <>
            <Layout title="Kreimben.com">
                <main>
                    <h1 className="">Home page</h1>
                    <p> { loremIpsum } </p>
                    <p> { loremIpsum } </p>
                </main>
            </Layout>
        </>
    )
}