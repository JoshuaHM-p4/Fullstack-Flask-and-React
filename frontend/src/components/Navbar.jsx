import { Container, Box, Flex, Text, Button, useColorMode, useColorModeValue } from '@chakra-ui/react';
import { IoMoon } from 'react-icons/io5';
import { LuSun } from 'react-icons/lu';


const Navbar = () => {
    const { colorMode, toggleColorMode } = useColorMode();
    return (
    <Container maxW={"80%"} marginTop={"0.5rem"}>
        <Box px={4} my={4} borderRadius={5} bg={useColorModeValue("gray.300", "gray.700")}>
            <Flex h="16" alignItems={"center"} justifyContent={"space-between"}>
                {/* left side */}
                <Flex alignItems={"center"} justifyContent={"center"} gap={3} display={{base: "none", sm: "flex"}}>
                    <img src="/react.png" alt="React Logo" width={50} height={50}/>
                    <Text fontSize={"40px"}>+</Text>
                    <img src="/python.png" alt="Python Logo" width={50} height={40}/>
                    <Text fontSize={"40px"}>=</Text>
                    <img src="/explode.png" alt="Exploding Head" width={45} height={45}/>
                </Flex>

                {/* right side */}
                <Flex gap={3} alignItems={"center"} >
                    <Text fontSize={"lg"} fontWeight={500} display={{base: "none", md:"block"}}>
                        BFF-SHIP🔥
                    </Text>
                    <Button onClick={toggleColorMode}>
                        {colorMode === "light" ? <IoMoon /> : <LuSun size={20}/>}
                    </Button>

                </Flex>
            </Flex>
        </Box>

    </Container>
  )
}

export default Navbar
