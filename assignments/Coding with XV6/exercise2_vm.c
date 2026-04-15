#include <stdio.h>
#include <stdint.h>

#define PAGE_SIZE 4096
#define OFFSET_MASK 0x0FFF
#define SHIFT_AMOUNT 12

int page_table[16] = { 5, 2, 8, -1, 12, 1, 9, 3, -1, 7, 4, 6, 10, 15, 11, 14 };

uint32_t translate_address(uint16_t virtual_address) {
    uint16_t page_number = virtual_address >> SHIFT_AMOUNT;
    uint16_t offset = virtual_address & OFFSET_MASK;

    int frame = page_table[page_number];

    if (frame == -1) {
        printf("Page Fault!\n");
        return 0;
    }

    return ((uint32_t)frame << SHIFT_AMOUNT) | offset;
}

int main() {
    uint16_t va1 = 0x1A2B;
    uint16_t va2 = 0x3004;

    printf("VA: 0x%04X -> PA: 0x%05X\n", va1, translate_address(va1));
    printf("VA: 0x%04X -> PA: 0x%05X\n", va2, translate_address(va2));

    return 0;
}