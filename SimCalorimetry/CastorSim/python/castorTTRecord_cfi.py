import FWCore.ParameterSet.Config as cms

simCastorTTRecord = cms.EDProducer("CastorTTRecord",
    CastorDigiCollection 	= cms.InputTag( 'simCastorDigis' ),
    CastorSignalTS			= cms.uint32(4),
    
    ttpBits           		= cms.vuint32( 60, 61, 62, 63 ), 
    TriggerBitNames       	= cms.vstring( 'L1Tech_CASTOR_0.v0',
    									   'L1Tech_CASTOR_TotalEnergy.v0',
    									   'L1Tech_CASTOR_EM.v0',
    									   'L1Tech_CASTOR_HaloMuon.v0'
    									  ),
    TriggerThresholds		= cms.vdouble(	50, # gap trgger threshold 
    										65000, # jet energy threshold per sector
    										1500, 100, # fist EM threshold, second HAD threshold for egamma trigger
    										50, # muon trigger threshold
    									 )
)
