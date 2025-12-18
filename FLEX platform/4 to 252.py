from opentrons import protocol_api, types

metadata = {
    'protocolName': '武汉大学-小瓶子测试-自定义耗材版',
    'author': 'OpentronsAI',
    'description': '使用Xiaohei自定义耗材的多阶段液体转移协议',
    'source': 'OpentronsAI'
}

requirements = {
    'robotType': 'Flex',
    'apiLevel': '2.20'
}

def run(protocol: protocol_api.ProtocolContext):
    # 定义自定义耗材（嵌入式方案）
    # 3孔管架 20mL
    custom_3tube = {
        "ordering": [["A1"], ["A2"], ["A3"]],
        "brand": {"brand": "Xiaohei", "brandId": ["Xiaohei"]},
        "metadata": {
            "displayName": "Xiaohei 3 Tube Rack with xiaohei 20 mL",
            "displayCategory": "tubeRack",
            "displayVolumeUnits": "µL",
            "tags": []
        },
        "dimensions": {"xDimension": 127, "yDimension": 85, "zDimension": 80},
        "wells": {
            "A1": {"depth": 70, "totalLiquidVolume": 20000, "shape": "circular", 
                   "diameter": 27.6, "x": 23.5, "y": 42.5, "z": 10},
            "A2": {"depth": 70, "totalLiquidVolume": 20000, "shape": "circular", 
                   "diameter": 27.6, "x": 63.5, "y": 42.5, "z": 10},
            "A3": {"depth": 70, "totalLiquidVolume": 20000, "shape": "circular", 
                   "diameter": 27.6, "x": 103.5, "y": 42.5, "z": 10}
        },
        "groups": [{
            "brand": {"brand": "xiaohei", "brandId": []},
            "metadata": {"wellBottomShape": "flat", "displayCategory": "tubeRack"},
            "wells": ["A1", "A2", "A3"]
        }],
        "parameters": {
            "format": "irregular", "quirks": [], "isTiprack": False,
            "isMagneticModuleCompatible": False,
            "loadName": "xiaohei_3_tuberack_20000ul"
        },
        "namespace": "custom_beta",
        "version": 1,
        "schemaVersion": 2,
        "cornerOffsetFromSlot": {"x": 0, "y": 0, "z": 0}
    }
    
    # 6孔管架 5mL
    custom_6tube = {
        "ordering": [["A1"], ["A2"], ["A3"], ["A4"], ["A5"], ["A6"]],
        "brand": {"brand": "Xiaohei", "brandId": ["Xiaohei"]},
        "metadata": {
            "displayName": "Xiaohei 6 Tube Rack with xiaohei 5 mL",
            "displayCategory": "tubeRack",
            "displayVolumeUnits": "µL",
            "tags": []
        },
        "dimensions": {"xDimension": 127, "yDimension": 85, "zDimension": 80},
        "wells": {
            "A1": {"depth": 80, "totalLiquidVolume": 5000, "shape": "circular", 
                   "diameter": 10, "x": 13.5, "y": 42.5, "z": 0},
            "A2": {"depth": 80, "totalLiquidVolume": 5000, "shape": "circular", 
                   "diameter": 10, "x": 33.5, "y": 42.5, "z": 0},
            "A3": {"depth": 80, "totalLiquidVolume": 5000, "shape": "circular", 
                   "diameter": 10, "x": 53.5, "y": 42.5, "z": 0},
            "A4": {"depth": 80, "totalLiquidVolume": 5000, "shape": "circular", 
                   "diameter": 10, "x": 73.5, "y": 42.5, "z": 0},
            "A5": {"depth": 80, "totalLiquidVolume": 5000, "shape": "circular", 
                   "diameter": 10, "x": 93.5, "y": 42.5, "z": 0},
            "A6": {"depth": 80, "totalLiquidVolume": 5000, "shape": "circular", 
                   "diameter": 10, "x": 113.5, "y": 42.5, "z": 0}
        },
        "groups": [{
            "brand": {"brand": "xiaohei", "brandId": []},
            "metadata": {"wellBottomShape": "u", "displayCategory": "tubeRack"},
            "wells": ["A1", "A2", "A3", "A4", "A5", "A6"]
        }],
        "parameters": {
            "format": "irregular", "quirks": [], "isTiprack": False,
            "isMagneticModuleCompatible": False,
            "loadName": "xiaohei_6_tuberack_5000ul"
        },
        "namespace": "custom_beta",
        "version": 1,
        "schemaVersion": 2,
        "cornerOffsetFromSlot": {"x": 0, "y": 0, "z": 0}
    }

        # 小容量96孔板 (每孔1000µL) - Xiaohei自定义
    plate_96_b3 = protocol.load_labware(
        'xiaohei_96_wellplate_1000ul', 
        'B3',
        namespace='custom_beta',
        version=1
    )
    plate_96_c3 = protocol.load_labware(
        'xiaohei_96_wellplate_1000ul', 
        'C3',
        namespace='custom_beta',
        version=1
    )
    plate_96_d3 = protocol.load_labware(
        'xiaohei_96_wellplate_1000ul', 
        'D3',
        namespace='custom_beta',
        version=1
    )
    
    # 加载吸头架 (1000 µL)
    tips_1000_1 = protocol.load_labware('opentrons_flex_96_tiprack_1000ul', 'A1')
    tips_1000_2 = protocol.load_labware('opentrons_flex_96_tiprack_1000ul', 'A2')
    tips_1000_3 = protocol.load_labware('opentrons_flex_96_tiprack_1000ul', 'B1')
    tips_1000_4 = protocol.load_labware('opentrons_flex_96_tiprack_1000ul', 'B2')
    
    # 使用嵌入式定义加载自定义耗材
    plate_3tube_c1 = protocol.load_labware_from_definition(custom_3tube, 'C1')
    plate_3tube_d1 = protocol.load_labware_from_definition(custom_3tube, 'D1')
    plate_6tube_c2 = protocol.load_labware_from_definition(custom_6tube, 'C2')
    plate_6tube_d2 = protocol.load_labware_from_definition(custom_6tube, 'D2')
    
    
    # 加载垃圾桶
    trash = protocol.load_trash_bin('A3')
    
    # 加载移液器 (8通道1000 µL)
    pipette_8ch = protocol.load_instrument(
        'flex_8channel_1000',
        mount='right',
        tip_racks=[tips_1000_1, tips_1000_2, tips_1000_3, tips_1000_4]
    )
    
    # 自定义多位置吸液函数
    def my_tr(pip, aspirate_1, aspirate_2, aspirate_3, aspirate_4, 
              aspirate_5, aspirate_6, aspirate_7, 
              aspirate_well, dispense_well, dispense_plate, mix=None):
        """从源孔的7个不同Y坐标位置依次吸液,然后分配到目标孔"""
        y_positions = [0, 9, 18, 27, 36, 45, 54]
        volumes = [aspirate_1, aspirate_2, aspirate_3, aspirate_4, 
                   aspirate_5, aspirate_6, aspirate_7]
        
        # 修正：使用 types.Point 而不是 protocol_api.types.Point
        for vol, y_pos in zip(volumes, y_positions):
            pip.aspirate(vol, aspirate_well.bottom(z=1).move(
                types.Point(x=0, y=y_pos, z=0)))
            pip.move_to(aspirate_well.top(z=10))
        
        pip.dispense(sum(volumes), 
                     dispense_plate[dispense_well].top(z=30),
                     rate=0.3)
        
        if mix:
            pip.mix(mix[0], mix[1], dispense_plate[dispense_well])
    
    # ========== 第一阶段:简单转移 ==========
    protocol.comment("=== 第一阶段:大容量3孔管架到中容量6孔管架 ===")
    
    # Group 1: C1-A1 → C2
    pipette_8ch.pick_up_tip(tips_1000_1['A1'])
    pipette_8ch.aspirate(800, plate_3tube_c1['A1'].bottom(z=1))
    pipette_8ch.dispense(800, plate_6tube_c2['A1'])
    pipette_8ch.aspirate(600, plate_3tube_c1['A1'].bottom(z=1))
    pipette_8ch.dispense(600, plate_6tube_c2['A2'])
    pipette_8ch.aspirate(400, plate_3tube_c1['A1'].bottom(z=1))
    pipette_8ch.dispense(400, plate_6tube_c2['A3'])
    pipette_8ch.aspirate(300, plate_3tube_c1['A1'].bottom(z=1))
    pipette_8ch.dispense(300, plate_6tube_c2['A4'])
    pipette_8ch.drop_tip()
    
    # Group 2: C1-A2 → C2
    pipette_8ch.pick_up_tip(tips_1000_1['A2'])
    pipette_8ch.aspirate(300, plate_3tube_c1['A2'].bottom(z=1))
    pipette_8ch.dispense(300, plate_6tube_c2['A5'])
    pipette_8ch.aspirate(500, plate_3tube_c1['A2'].bottom(z=1))
    pipette_8ch.dispense(500, plate_6tube_c2['A6'])
    pipette_8ch.drop_tip()
    
    # Group 3: D1-A1 → D2
    pipette_8ch.pick_up_tip(tips_1000_1['A3'])
    pipette_8ch.aspirate(800, plate_3tube_d1['A1'].bottom(z=1))
    pipette_8ch.dispense(800, plate_6tube_d2['A1'])
    pipette_8ch.aspirate(600, plate_3tube_d1['A1'].bottom(z=1))
    pipette_8ch.dispense(600, plate_6tube_d2['A2'])
    pipette_8ch.aspirate(400, plate_3tube_d1['A1'].bottom(z=1))
    pipette_8ch.dispense(400, plate_6tube_d2['A3'])
    pipette_8ch.aspirate(300, plate_3tube_d1['A1'].bottom(z=1))
    pipette_8ch.dispense(300, plate_6tube_d2['A4'])
    pipette_8ch.drop_tip()
    
    # Group 4: D1-A2 → D2
    pipette_8ch.pick_up_tip(tips_1000_1['A4'])
    pipette_8ch.aspirate(800, plate_3tube_d1['A2'].bottom(z=1))
    pipette_8ch.dispense(800, plate_6tube_d2['A5'])
    pipette_8ch.aspirate(600, plate_3tube_d1['A2'].bottom(z=1))
    pipette_8ch.dispense(600, plate_6tube_d2['A6'])
    pipette_8ch.drop_tip()
    
    # ========== 第二阶段:多位置吸液 ==========
    protocol.comment("=== 第二阶段:中容量6孔管架到小容量96孔板 ===")
    
    # Group 1: C2-A1 → B3 (A1-A6)
    pipette_8ch.pick_up_tip(tips_1000_2['A1'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A1'], 'A1', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_c2['A1'], 'A2', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A1'], 'A3', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A1'], 'A4', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A1'], 'A5', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A1'], 'A6', plate_96_b3)
    pipette_8ch.drop_tip()
    
    # Group 2: C2-A2 → B3 (A7-A12)
    pipette_8ch.pick_up_tip(tips_1000_2['A2'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A2'], 'A7', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_c2['A2'], 'A8', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A2'], 'A9', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A2'], 'A10', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A2'], 'A11', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A2'], 'A12', plate_96_b3)
    pipette_8ch.drop_tip()
    
    # Group 3: C2-A3 → B3 (A7-A12)
    pipette_8ch.pick_up_tip(tips_1000_2['A3'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A3'], 'A7', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_c2['A3'], 'A8', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A3'], 'A9', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A3'], 'A10', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A3'], 'A11', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A3'], 'A12', plate_96_b3)
    pipette_8ch.drop_tip()
    
    # Group 4: C2-A4 → B3 (A7-A12)
    pipette_8ch.pick_up_tip(tips_1000_2['A4'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A4'], 'A7', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_c2['A4'], 'A8', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A4'], 'A9', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A4'], 'A10', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A4'], 'A11', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A4'], 'A12', plate_96_b3)
    pipette_8ch.drop_tip()
    
    # Group 5: C2-A5 → B3 (A7-A12)
    pipette_8ch.pick_up_tip(tips_1000_2['A5'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A5'], 'A7', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_c2['A5'], 'A8', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A5'], 'A9', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A5'], 'A10', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A5'], 'A11', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A5'], 'A12', plate_96_b3)
    pipette_8ch.drop_tip()
    
    # Group 6: C2-A6 → B3 (A7-A12)
    pipette_8ch.pick_up_tip(tips_1000_2['A6'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A6'], 'A7', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_c2['A6'], 'A8', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A6'], 'A9', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A6'], 'A10', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A6'], 'A11', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_c2['A6'], 'A12', plate_96_b3)
    pipette_8ch.drop_tip()
    
    # Group 7: D2-A1 → B3/C3/D3
    pipette_8ch.pick_up_tip(tips_1000_2['A7'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A1'], 'A1', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_d2['A1'], 'A7', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A1'], 'A1', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A1'], 'A7', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A1'], 'A1', plate_96_d3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A1'], 'A7', plate_96_d3)
    pipette_8ch.drop_tip()
    
    # Group 8: D2-A2 → B3/C3/D3
    pipette_8ch.pick_up_tip(tips_1000_2['A8'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A2'], 'A2', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_d2['A2'], 'A8', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A2'], 'A2', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A2'], 'A8', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A2'], 'A2', plate_96_d3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A2'], 'A8', plate_96_d3)
    pipette_8ch.drop_tip()
    
    # Group 9: D2-A3 → B3/C3/D3
    pipette_8ch.pick_up_tip(tips_1000_2['A9'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A3'], 'A3', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_d2['A3'], 'A9', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A3'], 'A3', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A3'], 'A9', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A3'], 'A3', plate_96_d3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A3'], 'A9', plate_96_d3)
    pipette_8ch.drop_tip()
    
    # Group 10: D2-A4 → B3/C3/D3
    pipette_8ch.pick_up_tip(tips_1000_2['A10'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A4'], 'A4', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_d2['A4'], 'A10', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A4'], 'A4', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A4'], 'A10', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A4'], 'A4', plate_96_d3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A4'], 'A10', plate_96_d3)
    pipette_8ch.drop_tip()
    
    # Group 11: D2-A5 → B3/C3/D3
    pipette_8ch.pick_up_tip(tips_1000_2['A11'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A5'], 'A5', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_d2['A5'], 'A11', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A5'], 'A5', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A5'], 'A11', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A5'], 'A5', plate_96_d3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A5'], 'A11', plate_96_d3)
    pipette_8ch.drop_tip()
    
    # Group 12: D2-A6 → B3/C3/D3
    pipette_8ch.pick_up_tip(tips_1000_2['A12'])
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A6'], 'A6', plate_96_b3)
    my_tr(pipette_8ch, 40, 40, 40, 40, 40, 40, 40, 
          plate_6tube_d2['A6'], 'A12', plate_96_b3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A6'], 'A6', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A6'], 'A12', plate_96_c3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A6'], 'A6', plate_96_d3)
    my_tr(pipette_8ch, 50, 50, 50, 50, 50, 50, 50, 
          plate_6tube_d2['A6'], 'A12', plate_96_d3)
    pipette_8ch.drop_tip()
    
    protocol.comment("=== 协议完成 ===")