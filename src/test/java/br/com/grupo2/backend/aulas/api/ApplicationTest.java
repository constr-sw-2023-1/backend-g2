package br.com.grupo2.backend.aulas.api;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;


@ExtendWith(MockitoExtension.class)
class ApplicationTest {

    @Test
    void testaMain() {
        Application.main(new String[] {});
    }

}